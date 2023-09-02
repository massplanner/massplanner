# MassPlanner Development & Module Documentation

## Table of Contents
1. [Development Setup](#development-setup)
2. [Recommendations Module](#recommendations-module)

---

## Development Setup

### Prerequisites
- Git
- Python 3.x
- Pipenv
- PNPM

### Steps

1. **Clone the Repository**
    ```bash
    git clone https://github.com/massplanner/massplanner.git
    ```

2. **Navigate to Project Directory**
    ```bash
    cd massplanner
    ```

3. **Activate Virtual Environment**
    ```bash
    pipenv shell
    ```

4. **Install Python Dependencies**
    ```bash
    pipenv install
    ```

5. **Build the Project**
    ```bash
    pnpm build
    ```

---

## Recommendations Module

### Overview

The Recommendations Module uses Generative AI to provide insights on resumes. It extracts skills, titles, etc., and matches them against a pre-defined set of standardized occupations stored in a vector database. The system uses cosine similarity to compare these features in real-time and offers three different categories of recommendations based on skills, occupation titles, and raw resume text.

### Features

- `recommendations_by_generative_skills`: Suggestions based on skills.
- `recommendations_by_generative_occupation_titles`: Suggestions based on occupation titles.
- `recommendations_by_raw_resume_text`: Suggestions based on the raw text of the resume.

### Running Background Servers

Run the background services needed for the Recommendations module:

```bash
pnpm pnpm start:recommendations:background-services
```
