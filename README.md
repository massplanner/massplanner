Welcome to MassPlanner!

Working on some cool stuff for EthParis and EthNewYork, but let's talk about what we have right now.

We're bringing back a tool called [Mass Planner](https://www.fabionodariphoto.com/en/massplanner-gets-shut-down/) that used to be super popular, but we're making it even better! Our new tool is like a super-smart robot that's always looking for new and exciting things for you to learn and explore.

Auto Apply (Offline Aspect)
<img width="1546" alt="Screenshot 2023-09-04 at 5 24 08 PM" src="https://github.com/massplanner/massplanner/assets/17681450/e580f5da-81e6-4acf-bc08-513a154b4bc2">


Here's what our tool can do:

1. **Resume Feature Extraction**: Imagine you could have a robot read your resume and understand all the important stuff like your skills, your experience, and your education. That's exactly what this does! It uses something called machine learning (which is just a fancy way of saying it can learn from experience) to understand your resume.

2. **Resume Recommendations**: Once our robot understands your resume, it can suggest related skills you might want to learn, jobs you might be good at, and even YouTube videos to help you learn more. It's like having your own personal career advisor!

3. **YouTube Links**: Our robot can find YouTube videos related to the skills and jobs it thinks you might like. It's a great way to learn more about these areas.

4. **Interview Preparation Tips**: Going for a job interview can be scary, but our robot can give you tips to help you get ready and feel more confident.

5. **Suggested Improvements**: Our robot can even suggest ways to make your resume better. This can help you have a better chance of getting the job you want.

To use our tool, you need to send information to two places (we call these "endpoints"):

1. POST /api/features: This is where you send your resume. Our robot will read it and understand all the important stuff.

2. POST /api/recommendations: Once our robot understands your resume, it will send back a bunch of recommendations to help you improve and learn new things.

Don't worry if this sounds complicated. We've designed our tool to be super easy to use. And remember, our robot is here to help you learn and grow!

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
