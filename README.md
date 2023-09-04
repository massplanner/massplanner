massplanner ai

tl;dr im repurposing an old industry tool called [Mass Planner Gets Shutdown](https://www.fabionodariphoto.com/en/massplanner-gets-shut-down/) that got banned for public good. The new tool purpose is to continously search for new content for consumers but needs to be feed lol.

- 🎓 **Learn to Earn Mechanics**: Powered by the [Chia Network](https://www.chia.net/).
  - 💡 **Barrier-Free Entry**: We've removed the traditional stumbling blocks—UX complexity and initial financial investments—to make blockchain technology more accessible.
  - 💎 **Pay with Learning or Engagement**: Here, value is not just monetary. Contribute by learning or by actively participating in the platform. 
    - 👤 **Minimum Requirement**: Simply upload your resume to start earning network tokens.
    - 🛠 **Advanced Engagement**: Utilize our function-calling feature (enabled by OpenAI technology) to perform tasks based on zero-shot data. This action requires staking tokens, which you can earn initially by uploading your resume.
<img width="138" alt="Screenshot 2023-09-03 at 6 48 00 PM" src="https://github.com/massplanner/massplanner/assets/17681450/0e28c033-7402-48e2-b3c7-702047f30451">

- 🚀 **Speed & Efficiency**: The seeder is in prime condition and architected for dynamic adaptability across platforms.
  
- 📊 **Real-time Analytics**: All our data is sourced from trusted, public databases like the [BLS](https://www.bls.gov/), ensuring that you're always in the loop with real-time, accurate information.



## Features

- Resume Analysis
- Interview Preparation Tips
- Suggestions for Resume Improvements
- Generated Skills and Occupations
- Learning Resources Links

## Installation

### Build MassPlanner

First, clone the repository and navigate into the project directory. Then, execute the following command to build MassPlanner:

```bash
pnpm build
```

### Start the API

Start using the following command:

```bash
pnpm start:api
```

## Usage

### Uploading a Resume

To upload a resume and get recommendations, execute the following `curl` command:

```bash
curl --location 'http://localhost:8000/api/recommendations' \
--form 'document=@"/jack-sparrow-resume.pdf"'
```

You will receive a JSON response containing the analysis, suggestions, and links to resources to enhance your job search.


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
