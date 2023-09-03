from prisma import Prisma
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

prisma = Prisma()

async def create_resume(text, skills, occupations, text_embedding, skills_embedding, occupations_embedding, yt_links):
    logger.info("create_resume")
    await prisma.connect()

    result = await prisma.resume.create(data={
        "text": text,
        "occupations": str(occupations),
        "skills": str(skills),
        "yt_links": str(yt_links)
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


async def get_resume_embeddings(resume_id):
    logger.info("get_resume_embeddings")
    await prisma.connect()

    resume = await prisma.resume.find_unique(where={
        "id": resume_id
    })

    embeddings = await prisma.query_raw("""
    SELECT
        CAST(text_embedding AS TEXT) as text_embedding,
        CAST(skills_embedding AS TEXT) as skills_embedding,
        CAST(occupations_embedding AS TEXT) as occupations_embedding
    FROM resumes
    WHERE
        id = '{0}';
    """.format(resume.id))

    await prisma.disconnect()
    return embeddings
