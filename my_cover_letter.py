import os
import json
import datetime
import subprocess
from openai import OpenAI
from dotenv import load_dotenv
from jinja2 import Template

# === Load API key ===
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# === Load files ===
with open("profile.json", "r", encoding="utf-8") as f:
    profile = json.load(f)

with open("job_description.txt", "r", encoding="utf-8") as f:
    job_description = f.read()

# === Extract personal data ===
name = profile.get("name", "")
location = profile.get("location", "")
email = profile.get("email", "")
phone = profile.get("phone", "")
github = profile.get("github", "")
today = datetime.date.today().strftime("%B %d, %Y")

# === Ask GPT to generate body of the letter ===
prompt = f"""
You are a professional assistant.

Write a short, formal, ATS-friendly cover letter body based on the candidate profile and the job description.

Job:
{job_description}

Candidate:
{json.dumps(profile, indent=2)}

Guidelines:
- Don't make anything up
- Use only real skills
- Do not use abbrevations
- Do not non-English words
- Focus on fit and motivation
- Keep it under 350 words
- Only return the body, no greeting or closing
"""

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

body = response.choices[0].message.content.strip()

# === Load and render LaTeX template ===
with open("cover_letter_template.tex", "r", encoding="utf-8") as f:
    template = Template(f.read())

rendered = template.render(
    name=name,
    location=location,
    phone=phone,
    email=email,
    github=github,
    date=today,
    body=body
)

with open("cover_letter.tex", "w", encoding="utf-8") as f:
    f.write(rendered)

# === Compile LaTeX to PDF ===
subprocess.run(["pdflatex", "cover_letter.tex"])

print("✅ Cover letter generated and compiled: cover_letter.pdf")
