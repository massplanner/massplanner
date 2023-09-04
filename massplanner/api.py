#!/usr/local/bin/python3.9

from aiohttp import web
from dotenv import load_dotenv

load_dotenv()

from mp.recommendations import RecommendationsEngine
from mp.utils import set_files

import sys
import os
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


NANONETS_API_KEY = os.getenv('NANONETS_API_KEY')

async def get_features(request):
    headers = { "content_type": "application/json" }

    try:
        recommendations  = RecommendationsEngine(nanonets_api_key=NANONETS_API_KEY)
        document         = await request.json()
        features         = await recommendations.get_features_from_resume(document.get('id'), document.get('features'))

        return web.json_response({ "result": features }, headers=headers)
    except Exception as e:        
        logger.error(f"An error occurred while processing the resume: {str(e)}")
        return web.json_response({"error": "An error occurred while processing the resume. Please try again later."}, headers=headers, status=500)


@set_files
async def get_recommendations(request):
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

        resume_id             = await recommendations.create_resume(
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
        logger.error(f"An error occurred while processing the resume: {str(e)}")
        return web.json_response({"error": "An error occurred while processing the resume. Please try again later."}, headers=headers, status=500)

app = web.Application()

app.add_routes([
    web.post("/api/features", get_features),
    web.post("/api/recommendations", get_recommendations),
])

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
web.run_app(app, port=port)