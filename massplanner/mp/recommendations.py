from .utils import encode
from .prisma import get_resume_embeddings, create_resume, get_resume_text
from .openai import openai, GptFunction, GptFunctionParameter, GptFunctionParameterProperty, get_features_from_document

import json
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RecommendationsEngine:
    def __init__(self, resume_id=None, nanonets_api_key="None"):
        self.resume_id = resume_id
        self.nanonets_api_key = (nanonets_api_key + ":")
        logger.info("initialized")

    async def get_document_full_text(self, document):
        logger.info("get_document_full_text")
        data = {'file': document.file.read()}
        headers = {
            'Authorization': 'Basic ' + encode(self.nanonets_api_key),
        }
        config = {
            'method': 'post',
            'url': 'https://app.nanonets.com/api/v2/OCR/FullText',
            'headers': headers,
            'files': data
        }
        response = requests.post(
            config['url'], headers=config['headers'], files=config['files'])
        result = response.json()

        if "errors" in result:
            return {
                "success": False,
                "result": result["errors"][0]["reason"]
            }
        else:
            return {
                "success": True,
                "result": response.json()['results'][0]['page_data'][0]['raw_text']
            }

    async def get_document_embedding(self, text, model="text-embedding-ada-002"):
        logger.info("get_document_embedding")
        text = text.replace("\n", " ")
        return openai.Embedding.create(input=[text], model=model)['data'][0]['embedding']

    async def get_labels_from_resume_text(self, resume_text, model='gpt-3.5-turbo-0613'):
        logger.info("get_labels_from_resume_text")
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
        parameter.add_property(GptFunctionParameterProperty(
            name="generated_recommended_youtube_links",
            type="string",
            description="String array of generated recommended youtube links based on the resume text.",
            example="[a youtube link to what is python, a youtube link to what is business development, etc...]"
        ))
        parameter.add_property(GptFunctionParameterProperty(
            name="interview_preperation_receipe",
            type="string",
            description="A step-by-step guide on how to prepare for an interview based on the skills and occupations extracted from the resume text.",
            example="Step 1: Review the job description and note down the required skills and experiences. Step 2: Research the company, understand their culture and work environment. Step 3: Prepare examples from your past experience that align with the job requirements. Step 4: Practice common interview questions and prepare your responses. Step 5: Plan your attire and ensure it fits the company culture. Step 6: Prepare questions to ask the interviewer. Remember, an interview is a two-way street."
        ))
        parameter.add_property(GptFunctionParameterProperty(
            name="suggested_improvements",
            type="string",
            description="String array of improvements suggested by the user based on their original resume.",
            example="['Too much custimization', 'Improve format', 'Include more personal projects']"
        ))

        function = GptFunction(
            name="build_gerative_profile_from_resume",
            description="extracts the required information from the resume text",
            parameter=parameter
        )

        messages = [
            {"role": "user", "content": "Gather the relevant information from the resume text to be used for an embedding: " + resume_text}]
        functions = [function.get_serialized()]

        logger.info("get_labels_from_resume_text::chat_response")
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

    async def create_resume(self,
                            resume_text,
                            skills,
                            occupations,
                            resume_embedding,
                            skills_embedding,
                            occupations_embedding,
                            yt_links):
        return await create_resume(
            resume_text,
            skills,
            occupations,
            resume_embedding,
            skills_embedding,
            occupations_embedding,
            yt_links
        )

    async def get_occupation_recommendations(self):
        return await get_resume_embeddings(self.resume_id)
    
    async def get_features_from_resume(self, resume_id, features):
        resume_text = await get_resume_text(resume_id)
        return await get_features_from_document(resume_text, features)
