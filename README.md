MassPlanner

EthParis https://ethglobal.com/showcase/parity-b6mkg  
EthNewYork currently doing discovery on directions this could go

tl;dr im repurposing an old industry tool called [Mass Planner Gets Shutdown](https://www.fabionodariphoto.com/en/massplanner-gets-shut-down/) that got banned for public good. The new tool purpose is to continously search for new content for consumers but needs to be feed lol.


Next Auto Apply (Offline Aspect)
<img width="1546" alt="Screenshot 2023-09-04 at 5 24 08 PM" src="https://github.com/massplanner/massplanner/assets/17681450/e580f5da-81e6-4acf-bc08-513a154b4bc2">



Resume Feature Extraction and Resume Recommendations. 
=======

The Resume Feature Extraction functionality uses advanced machine learning techniques to extract key features such as skills, experience, education, and more from a resume. The extracted features are then used by the Resume Recommendations functionality to generate potential related skills and occupations, provide recommended YouTube links for learning, offer interview preparation tips, and suggest improvements for the resume.

The API provides two endpoints: 
- POST /api/features: This endpoint accepts a JSON object with an 'id' and 'features' of a resume and returns the extracted features.
- POST /api/recommendations: This endpoint accepts a resume document and returns a set of recommendations.

To use the MassPlanner API, you need to have Python 3.9 and aiohttp installed. You also need to set the NANONETS_API_KEY environment variable to your Nanonets API key.The MassPlanner API is a powerful tool designed to assist in resume analysis and recommendation generation. It utilizes advanced machine learning techniques to extract key features from resumes, generate potential related skills and occupations, and provide valuable recommendations to enhance the resume. 

## Features

1. Resume Feature Extraction: Extracts key features from a resume, such as skills, experience, education, and more. This is done using the Nanonets API, a powerful machine learning service.

2. Resume Recommendations: Based on the extracted features, the engine generates potential related skills and occupations. This can help users understand what skills they might need to develop or what occupations they might be suitable for.

3. YouTube Links: The engine generates recommended YouTube links related to the potential skills and occupations. This can help users learn more about these areas.

4. Interview Preparation Tips: The engine provides interview preparation tips based on the resume's content. This can help users prepare for job interviews.

5. Suggested Improvements: The engine suggests improvements for the resume. This can help users enhance their resumes and increase their chances of getting a job.

## API Endpoints

1. POST /api/features: This endpoint accepts a JSON object with an 'id' and 'features' of a resume. It returns the extracted features from the resume.

2. POST /api/recommendations: This endpoint accepts a resume document and returns a set of recommendations, including potential related skills, occupations, YouTube links, interview preparation tips, and suggested improvements.

## Examples

```json
{
    "result": {
        "resume_id": "clm3vjhv50000qq5fznh3br9u",
        "interview_preperation": "1. Research the company and its mission.\n2. Review common interview questions.\n3. Prepare your own questions to ask the interviewer.\n4. Practice your answers and skills.\n5. Dress professionally and arrive early.\n6. Relax and be confident during the interview.",
        "suggested_improvements": [
            "Provide more specific details about accomplishments and responsibilities.",
            "Include education dates and institution names.",
            "Highlight specific programming languages and technologies used."
        ],
        "generated": {
            "skills": [
                "Captain",
                "Black Pearl",
                "East Indies",
                "Tortuga",
                "Programming",
                "html",
                "css",
                "python",
                "javascript",
                "R",
                "Android",
                "Linux",
                "Bucaneering",
                "Pirate",
                "Certified",
                "English",
                "French",
                "Spanish",
                "Italian"
            ],
            "occupations": [
                "Captain",
                "Pirate",
                "Programmer",
                "Web Developer"
            ],
            "links": {
                "youtube": [
                    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                    "https://www.youtube.com/watch?v=9bZkp7q19f0",
                    "https://www.youtube.com/watch?v=kXYiU_JCYtU"
                ]
            }
        }
    }
}
```

ZeroShot Configs
```json
[
    {
        
        "name": "personal_details",
        "type": "object",
        "description": "Personal details of the user including name, contact, and address.",
        "example": {"name": "John Doe", "email": "johndoe@example.com", "phone": "123-456-7890", "address": "123 Main St, City, Country"}
    },
    {
        "name": "educational_background",
        "type": "array",
        "description": "List of educational institutions attended, degrees achieved, and years.",
        "example": [{"institution": "XYZ University", "degree": "B.Sc. Computer Science", "year": "2015-2019"}]
    },
    {
        "name": "professional_experience",
        "type": "array",
        "description": "List of jobs held, including company name, role, duration, and key achievements.",
        "example": [{"company": "ABC Corp.", "role": "Software Developer", "duration": "2019-2021", "achievements": ["Developed X feature", "Improved Y process"]}]
    },
    {
        "name": "skills_and_certifications",
        "type": "array",
        "description": "List of skills, languages, tools, and certifications possessed by the user.",
        "example": ["Python", "Machine Learning", "Certified Scrum Master"]
    },
    {
        "name": "publications_and_projects",
        "type": "array",
        "description": "List of publications, research work, or projects undertaken.",
        "example": [{"title": "Research on X", "published_in": "Journal Y", "year": "2020"}]
    },
    {
        "name": "volunteer_work",
        "type": "array",
        "description": "List of volunteer activities, roles, and organizations.",
        "example": [{"organization": "Helping Hands", "role": "Coordinator", "duration": "2018-2019"}]
    },
    {
        "name": "awards_and_achievements",
        "type": "array",
        "description": "List of awards, honors, and significant achievements.",
        "example": ["Best Employee of the Year 2020", "Winner of Z Hackathon"]
    },
    {
        "name": "references",
        "type": "array",
        "description": "List of professional references including name, relation, contact details.",
        "example": [{"name": "Jane Smith", "relation": "Former Manager", "contact": "jane@example.com"}]
    },
    {
        "name": "personal_interests",
        "type": "array",
        "description": "List of hobbies, interests, and non-professional activities.",
        "example": ["Reading", "Hiking", "Photography"]
    },
    {
        "name": "language_proficiency",
        "type": "array",
        "description": "List of languages known and proficiency level.",
        "example": [{"language": "English", "proficiency": "Fluent"}, {"language": "Spanish", "proficiency": "Intermediate"}]
    },
    {
        "name": "personal_statement_or_objective",
        "type": "string",
        "description": "Brief personal statement or career objective of the user.",
        "example": "A motivated software engineer with 5 years of experience looking to contribute to innovative projects."
    },
    {
        "name": "public_contributions",
        "type": "object",
        "description": "Details of contributions to public goods, open source projects, community services, etc.",
        "example": {"open_source": ["Project X on GitHub"], "community_service": ["Organized Tech for Good Event"]}
    },
    {
        "name": "digital_footprint",
        "type": "array",
        "description": "Links to user's online profiles, portfolios, blogs, or any other relevant platforms.",
        "example": ["https://linkedin.com/in/johndoe", "https://github.com/johndoe"]
    }
]
```
