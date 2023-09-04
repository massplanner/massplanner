Welcome to MassPlanner!

We're working on some cool stuff for EthParis and EthNewYork, but let's talk about what we have right now.

We're bringing back a tool called [Mass Planner](https://www.fabionodariphoto.com/en/massplanner-gets-shut-down/) that used to be super popular, but we're making it even better! Our new tool is like a super-smart robot that's always looking for new and exciting things for you to learn and explore.

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
