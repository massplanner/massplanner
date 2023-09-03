from .lib import encode, GptFunction, GptFunctionParameter, GptFunctionParameterProperty
from .db import prisma
from dotenv import load_dotenv
load_dotenv()

import os
import json
import requests
import logging
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
NANONETS_API_KEY = (os.getenv("NANONETS_API_KEY") + ":")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RecommendationsEngine:
  def __init__(self):
    logger.info("Starting RecommendationsEngine...")

  async def get_document_full_text(self, document):
    data = {'file': document.file.read() }
    headers = {
      'Authorization': 'Basic ' + encode(NANONETS_API_KEY),
    }
    config = {
      'method': 'post',
      'url': 'https://app.nanonets.com/api/v2/OCR/FullText',
      'headers': headers,
      'files': data
    }
    response = requests.post(config['url'], headers=config['headers'], files=config['files'])
    return response.json()['results'][0]['page_data'][0]['raw_text']
  
  async def get_text_embedding(self, text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)['data'][0]['embedding']

  async def get_labels_from_resume_text(self, resume_text, model='gpt-3.5-turbo-0613'):
    parameter = GptFunctionParameter(type="object")

    parameter.add_property(GptFunctionParameterProperty(
        name="potential_related_skills",
        type="string",
        description="String array of skills extracted from the resume text.",
        example="[Python, Forklift Machine, ...]"
    ))
    parameter.add_property(GptFunctionParameterProperty(
        name="potential_related_occupations",
        type="string",
        description="String array of occupations extracted from the resume text.",
        example="[JR Developer, Head of Business Development, ...]"
    ))

    function = GptFunction(
        name="extract_information_from_resume",
        description="extracts the required information from the resume text",
        parameter=parameter
    )

    messages  = [{"role": "user", "content": "Gather the relevant information from the resume text to be used for an embedding: " + resume_text}]
    functions = [function.get_serialized()]

    chat_response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        functions=functions,
        function_call="auto",
    )

    chat_response_message = chat_response["choices"][0]["message"]

    if chat_response_message.get("function_call"):
        return {
            "success": True,
            "result": json.loads(chat_response_message["function_call"]["arguments"])
        }
    else:
        return {
            "success": False,
            "result": chat_response_message
        }
    
  async def create_resume(self, text, skills, occupations, text_embedding, skills_embedding, occupations_embedding):
    await prisma.connect()

    result = await prisma.resume.create(data={
      "text": text,
      "occupations": str(occupations),
      "skills": str(skills)
    })

    await prisma.query_raw("""
    UPDATE resumes
    SET
      text_embedding = '{0}'::vector,
      skills_embedding = '{1}'::vector,
      occupations_embedding = '{2}'::vector            
    WHERE
      id = '{3}';
    """.format(text_embedding, skills_embedding, occupations_embedding, result.id))

    await prisma.disconnect()
    return result.id
  
  async def get_resume_occupation_recommendations(self, resume_id):
    await prisma.connect()

    resume = await prisma.resume.find_unique(where={
      "id": resume_id
    })

    embeddings = await prisma.query_raw("""
    SELECT
      CAST(text_embedding AS TEXT) as text_embedding,
      CAST(skills_embedding AS TEXT) as skills_embedding,
      CAST(occupations_embedding AS TEXT) as occupations_embedding,
    FROM resumes
    WHERE
      id = '{0}';
    """.format(resume.id))

    await prisma.disconnect()
    return