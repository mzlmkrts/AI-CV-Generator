# AI-CV-Generator


AI-Powered CV & Cover-Letter Generator
A command-line tool that takes your profile JSON and a job description, calls OpenAI to optimize your CV for ATS, renders a LaTeX template, and compiles a beautifully formatted PDF résumé.

🔍 Features
Strict mode for exact ATS-friendly formatting (no new content).

Creative mode for human-friendly rewording + ATS optimization.

Auto-filters to show your top 6 most relevant skills.

LaTeX template–based styling → high-quality PDF output.

Simple CLI interaction.

🚀 Quick Start
Clone the repo
git clone https://github.com/yourusername/AI-CV-CoverGen.git
cd AI-CV-CoverGen

Configure your environment
Copy .env.example to .env, then add your OpenAI API key:
cp .env.example .env

edit .env and set OPENAI_API_KEY=your_api_key_here
Install dependencies
pip install -r requirements.txt

Ensure LaTeX is installed
You need a working TeX distribution with pdflatex.

Ubuntu/Debian
sudo apt update
sudo apt install texlive-latex-base texlive-fonts-recommended texlive-latex-extra

macOS (with Homebrew)
brew install --cask mactex-no-gui

Prepare your inputs

profile.json — your personal data, education, experience, etc.

job_description.txt — plain-text job posting.

Run the generator
python generate_cv.py
You’ll be prompted for mode:

vbnet
Kopyala
Düzenle
Which mode do you want to use? (strict/creative):
View your résumé
After compilation, open generated_cv.pdf in your default PDF viewer.

⚙️ Project Structure
.
├── modern_cv_template.tex # Jinja2-powered LaTeX template
├── generate_cv.py # Main script
├── profile.json # Example profile
├── job_description.txt # Example job posting
├── requirements.txt # Python dependencies
├── .env.example # Template for your OpenAI key
└── README.md # You are here

🛠️ Dependencies
Python packages
openai

jinja2

python-dotenv

(Install with pip install -r requirements.txt)

System tools
pdflatex (part of any standard LaTeX distribution)

Git (for cloning and version control)

✏️ Customization
Template: edit modern_cv_template.tex (Jinja2 tags) to adjust layout, fonts, colors.

Prompt logic: tweak the prompt strings inside generate_cv.py to suit your tone or ATS rules.

Skill filtering: change the number of skills shown by modifying the slicing logic in the script.

📄 License
This project is released under the MIT License.

🙏 Acknowledgments
Uses the OpenAI API for text generation.

Built on top of Jinja2 and LaTeX for flexible, professional formatting.

Happy résumé-building! 🚀
