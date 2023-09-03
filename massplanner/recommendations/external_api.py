#!/usr/local/bin/python3.9
from aiohttp import web
from dotenv import load_dotenv

load_dotenv()
from src.lib import set_files
from src.engine import RecommendationsEngine

import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@set_files
async def get_document_full_text(request):
    headers = { "content_type": "text/html" }

    recommendations = RecommendationsEngine()
    resume_document = request.files.get('document')
    response        = await recommendations.get_document_full_text(resume_document)

    return web.json_response({ "result": response }, headers=headers)


async def get_text_embedding(request):
    headers = { "content_type": "application/json" }

    recommendations = RecommendationsEngine()
    document        = await request.json()
    response        = await recommendations.get_text_embedding(document['text'])

    return web.json_response({ "result": response }, headers=headers)
  

@set_files
async def upload_resume(request):
    headers = { "content_type": "application/json" }

    try:
        recommendations  = RecommendationsEngine()
        resume_document  = request.files.get('document')
        resume_text      = await recommendations.get_document_full_text(resume_document)
        extracted_labels = await recommendations.get_labels_from_resume_text(resume_text)

        if not extracted_labels['success']:
            return web.json_response({ "result": extracted_labels['result'] }, headers=headers)

        resume_embedding      = await recommendations.get_text_embedding(resume_text)
        skills_embedding      = await recommendations.get_text_embedding(",".join(extracted_labels['result']['potential_related_skills']))
        occupations_embedding = await recommendations.get_text_embedding(",".join(extracted_labels['result']['potential_related_occupations']))

        resume_id = await recommendations.create_resume(
            resume_text, 
            extracted_labels['result']['potential_related_skills'], 
            extracted_labels['result']['potential_related_occupations'], 
            resume_embedding, 
            skills_embedding, 
            occupations_embedding
        )
        
        return web.json_response({ "result": resume_id }, headers=headers)
    except Exception as e:
        return web.json_response({ "result": str(e) }, headers=headers)



app = web.Application()
app.add_routes([
    web.post("/api/recommendations/upload-resume", upload_resume),
    web.post("/api/recommendations/document-full-text", get_document_full_text),
    web.post("/api/recommendations/text-embedding", get_text_embedding),
])
web.run_app(app, port=8000)