# AI-Powered CV & Cover-Letter Generator

A command-line tool that takes your `profile.json` and a job description, uses the OpenAI API to generate a tailored, ATS-optimized CV **and** a formal cover letter, compiles both from LaTeX templates, and outputs professional PDF files.

---

## 🔍 Features

- ✅ **Strict mode**: ATS-optimized CV without adding any new content  
- ✅ **Creative mode**: Improves clarity and rewords slightly while remaining ATS-friendly  
- ✅ Generates a professional **cover letter body** based strictly on your profile  
- ✅ Clean, customizable **LaTeX** templates for both CV and cover letter  
- ✅ Produces print-ready **PDF files** in seconds

---

## 🚀 Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/AI-CV-Generator.git
   cd AI-CV-Generator
   ```

2. **Add your OpenAI API key**

   ```bash
   cp .env.example .env
   ```
   Then open `.env` and set:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install LaTeX (`pdflatex`)**

   You need a working LaTeX installation:

   - **Ubuntu / Debian**
     ```bash
     sudo apt update
     sudo apt install texlive-latex-base texlive-fonts-recommended texlive-latex-extra
     ```

   - **macOS (Homebrew)**
     ```bash
     brew install --cask mactex-no-gui
     ```

   - **Windows**
     Download and install [MiKTeX](https://miktex.org/download)

5. **Prepare your input files**

   - `profile.json` — your structured profile (name, contact info, education, experience, etc.)
   - `job_description.txt` — plain text job ad

---

## 📄 How to Generate Your CV

```bash
python generate_cv.py
```

You’ll be prompted to choose between:

```
Which mode do you want to use? (strict/creative):
```

Once completed, your CV will be saved as:

```
generated_cv.pdf
```

---

## 📨 How to Generate Your Cover Letter

```bash
python generate_cover_letter.py
```

This generates a personalized cover letter and saves the output as:

```
cover_letter.pdf
```

---

## 📁 Project Structure

```
.
├── generate_cv.py               # CV generator script
├── generate_cover_letter.py     # Cover letter generator script
├── modern_cv_template.tex       # LaTeX CV template
├── cover_letter_template.tex    # LaTeX cover letter template
├── profile.json                 # Your profile data
├── job_description.txt          # Job ad to match
├── requirements.txt             # Python dependencies
├── .env.example                 # Sample .env file
└── README.md                    # This file
```

---

## 🛠️ Dependencies

### Python packages

- `openai`
- `jinja2`
- `python-dotenv`

Install them with:

```bash
pip install -r requirements.txt
```

### System tools

- `pdflatex` (from TeX Live, MacTeX, or MiKTeX)
- `git` (optional, for cloning)

---

## ✏️ Customization

| To change...                     | Edit...                          |
|----------------------------------|----------------------------------|
| Layout or styling                | `*.tex` templates                |
| GPT behavior or instructions     | Prompt strings in Python scripts |
| Number of skills shown in CV     | `skills = all_skills[:6]`       |

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgements

- Powered by the [OpenAI API](https://platform.openai.com)
- Built with [Jinja2](https://jinja.palletsprojects.com/) and [LaTeX](https://www.latex-project.org)

---

🎯 Build your best CV and cover letter — ready to impress recruiters and beat the bots.
