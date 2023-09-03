#!/usr/local/bin/python3.9
from aiohttp import web
from dotenv import load_dotenv

load_dotenv()

from lib import set_files
from lib.database import create_resume
from recommendations import RecommendationsEngine

import logging
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

NANONETS_API_KEY = os.getenv('NANONETS_API_KEY')

@set_files
async def get_document_full_text(request):
    headers = { "content_type": "text/html" }

    recommendations = RecommendationsEngine(nanonets_api_key=NANONETS_API_KEY)
    resume_document = request.files.get('document')
    response        = await recommendations.get_document_full_text(resume_document)
    
    return web.json_response(response, headers=headers)
    

async def get_document_embedding(request):
    headers = { "content_type": "application/json" }

    recommendations = RecommendationsEngine(nanonets_api_key=NANONETS_API_KEY)
    document        = await request.json()
    response        = await recommendations.get_document_embedding(document['text'])

    return web.json_response({ "result": response }, headers=headers)


async def get_occupation_recommendations(request):
    headers         = { "content_type": "application/json" }
    recommendations = RecommendationsEngine(resume_id=request.query.get('resume_id'), nanonets_api_key=NANONETS_API_KEY)
    embeddings      = await recommendations.get_occupation_recommendations()

    return web.json_response({ "result": embeddings }, headers=headers)


@set_files
async def document_upload(request):
    headers = { "content_type": "application/json" }

    try:
        recommendations  = RecommendationsEngine(nanonets_api_key=NANONETS_API_KEY)
        resume_document  = request.files.get('document')
        resume_text      = await recommendations.get_document_full_text(resume_document)

        if not resume_text["success"]:
            return web.json_response(resume_text, headers=headers)
        
        resume_text      = resume_text["result"]
        extracted_labels = await recommendations.get_labels_from_resume_text(resume_text)

        if not extracted_labels['success']:
            return web.json_response(extracted_labels['result'], headers=headers)
        
        skills                 = extracted_labels['result']['potential_related_skills']
        occupations            = extracted_labels['result']['potential_related_occupations']
        yt_links               = extracted_labels['result']['generated_recommended_youtube_links']
        interview_preperation  = extracted_labels['result']['interview_preperation_receipe']
        suggested_improvements = extracted_labels['result']['suggested_improvements']

        resume_embedding      = await recommendations.get_document_embedding(resume_text)
        skills_embedding      = await recommendations.get_document_embedding("{}".format(",".join(skills)))
        occupations_embedding = await recommendations.get_document_embedding("{}".format(",".join(occupations)))

        resume_id = await create_resume(
            resume_text, 
            skills, 
            occupations, 
            resume_embedding, 
            skills_embedding, 
            occupations_embedding,
            yt_links
        )
        
        return web.json_response({ "result": {
            "resume_id": resume_id,
            "interview_preperation": interview_preperation,
            "suggested_improvements": suggested_improvements,
            "generated": {
                "skills": skills,
                "occupations": occupations,
                "links": {
                    "youtube": yt_links
                }
            },
        } }, headers=headers)
    except Exception as e:
        logger.info(e)
        return web.json_response({ "result": "" }, headers=headers)


app = web.Application()
app.add_routes([
    web.post("/api/document/upload", document_upload),
    web.post("/api/document/full-text", get_document_full_text),
    web.post("/api/document/embedding", get_document_embedding),
    web.get("/api/recommendations/occupations", get_occupation_recommendations),
])
web.run_app(app, port=8000)