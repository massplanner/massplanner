#!/usr/local/bin/python3.9
from aiohttp import web
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
import requests


console = Console()

def main():
    while True:
        console.print("Welcome to MassPlanner", style="bold blue")
        console.print("[1] Upload Resume")
        console.print("[2] Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            upload_resume()
        elif choice == '2':
            break
        else:
            console.print("Invalid option", style="bold red")

def upload_resume():
    # For now, let's keep the file name hardcoded
    file_path = "your_resume.pdf"
    url = 'http://localhost:8000/api/document/upload'

    files = {'document': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        display_results(response.json())
    else:
        console.print(f"Failed to upload resume. Error: {response.text}", style="bold red")

def display_results(data):
    result = data.get('result', {})
    resume_id = result.get('resume_id', 'N/A')
    
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Resume ID")
    table.add_column("Interview Preparation")
    table.add_column("Improvements")
    
    interview_prep = result.get('interview_preperation', 'N/A')
    suggested_improvements = result.get('suggested_improvements', [])
    suggested_improvements_str = "\n".join(suggested_improvements)
    
    table.add_row(resume_id, interview_prep, suggested_improvements_str)
    console.print(table)

if __name__ == '__main__':
    main()
