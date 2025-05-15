import os
import json
import subprocess
from openai import OpenAI
from jinja2 import Template
from dotenv import load_dotenv

# === Load .env and OpenAI API key ===
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# === Prompt user for mode and template ===
mode = input("Which mode do you want to use? (strict/creative): ").strip().lower()

template_path = "modern_cv_template.tex" 

# === Load input files ===
with open("profile.json", "r", encoding="utf-8") as f:
    profile = json.load(f)

with open("job_description.txt", "r", encoding="utf-8") as f:
    job_description = f.read()

# === GPT prompt ===
if mode == "strict":
    prompt = f"""
You are optimizing a CV for ATS (Applicant Tracking Systems).

Given this profile:
{json.dumps(profile, indent=2)}

And this job description:
{job_description}

IMPORTANT:
- Only use information in the profile.
- Do not invent or add anything new.
- Rewrite experience as 3 bullet points per job.
- Prioritize relevant skills.
- Rewrite the "about_me" section to match the job and highlight key qualifications but do not invent or add anything new.
- Always include the following fields: name, email, phone, education, experience, skills, languages.

Return a JSON object in this format:
{{
  "name": "...",
  "email": "...",
  "phone": "...",
  "webpage": "...",
  "location": "...",
  "about_me": "...",
  "github": "...",
  "education": [...],
  "experience": [
    {{
      "position": "...",
      "company": "...",
      "years": "...",
      "details": ["...", "..."]
    }}
  ],
  "skills": ["...", "..."],
  "Languages": ["...", "..."]
}}
"""
else:
    prompt = f"""
You are helping optimize a CV for ATS (Applicant Tracking Systems).

Given this profile:
{json.dumps(profile, indent=2)}

And this job description:
{job_description}

- Feel free to slightly reword for clarity and ATS optimization.
- Rewrite experience as 3 bullet points per job.
- Prioritize relevant skills.
- Rewrite the "about_me" section to match the job and highlight key qualifications.
- Always include the following fields: name, email, phone, education, experience, skills, languages.

Return a JSON object in this format:
{{
  "name": "...",
  "email": "...",
  "phone": "...",
  "webpage": "...",
  "location": "...",
  "about_me": "...",
  "github": "...",
  "location": "...",
  "education": [...],
  "experience": [...],
  "skills": [...],
  "Languages": [...]
}}
"""

# === Call GPT and parse response ===
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

raw_output = response.choices[0].message.content
print("[DEBUG] GPT Output:\n", raw_output)
optimized_profile = json.loads(raw_output)

# === Filter top 6 relevant skills ===
all_skills = optimized_profile.get("skills", [])
skills = all_skills[:6] if isinstance(all_skills, list) else []

# === Load and render LaTeX template ===
with open(template_path, "r", encoding="utf-8") as f:
    template = Template(f.read())

rendered_latex = template.render(
    name=optimized_profile.get("name", ""),
    email=optimized_profile.get("email", ""),
    phone=optimized_profile.get("phone", ""),
    webpage=optimized_profile.get("webpage", ""),
    github=optimized_profile.get("github", ""), 
    location=optimized_profile.get("location", ""),
    about_me=optimized_profile.get("about_me", ""),
    education=optimized_profile.get("education", []),
    experience=optimized_profile.get("experience", []),
    skills=skills,
    Languages=optimized_profile.get("Languages", [])
)

with open("generated_cv.tex", "w", encoding="utf-8") as f:
    f.write(rendered_latex)

print("\n✅ LaTeX file generated as 'generated_cv.tex'")
print("🔧 Compiling LaTeX to PDF...")

# === Compile PDF with pdflatex ===
subprocess.run(["pdflatex", "generated_cv.tex"], stdout=subprocess.DEVNULL)

# === Open the PDF
pdf_path = os.path.abspath("generated_cv.pdf")
if os.name == "nt":
    os.startfile(pdf_path)
else:
    print(f"🖨️  Your CV is ready at: {pdf_path}")
