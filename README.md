massplanner

- 🌱 **Learn to Earn Mechanics**: Powered by the [Chia Network](https://www.chia.net/).
- 🚀 **Speed & Efficiency**: The seeder is in a working state and set to adapt to dynamic, cross-platform requirements.
- 📊 **Real-time Analytics**: Data sourced from publicly available datasets, like the [BLS](https://www.bls.gov/).

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
python massplanner/external_gateway_api.py
```

## Usage

### Uploading a Resume

To upload a resume and get recommendations, execute the following `curl` command:

```bash
curl --location 'http://localhost:8000/api/document/upload' \
--form 'document=@"/x/chrisbradley/jack-sparrow-resume.pdf"'
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
