# AI-Powered CV & Cover-Letter Generator

A command-line tool that takes your `profile.json` and a job description, uses the OpenAI API to generate a tailored, ATS-optimized **CV** and **cover letter**, compiles them from LaTeX templates, and outputs professional PDF files.

---

## 🔍 Features

- ✅ **Strict mode**: ATS-optimized CV using only your data  
- ✅ **Creative mode**: Enhanced readability while remaining factual and ATS-friendly  
- ✅ Generates a personalized **cover letter** using real profile content only  
- ✅ Clean, customizable **LaTeX** templates  
- ✅ Produces high-quality **PDFs** for CV and cover letter

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

## 📄 Generate Your CV

Run the CV generation script:

```bash
python generate_cv.py
```

You'll be asked:

```
Which mode do you want to use? (strict/creative):
```

The result is saved as:

```
generated_cv.pdf
```

---

## 📨 Generate Your Cover Letter

Run the cover letter generation script:

```bash
python my_cover_letter.py
```

This uses GPT-4 to generate a short, formal letter body from your `profile.json` and `job_description.txt`, then compiles the final version as:

```
cover_letter.pdf
```

---

## 📁 Project Structure

```
.
├── generate_cv.py               # CV generator script
├── my_cover_letter.py           # Cover letter generator script
├── modern_cv_template.tex       # LaTeX CV template
├── cover_letter_template.tex    # LaTeX cover letter template
├── profile.json                 # Your profile data
├── job_description.txt          # Job ad description
├── requirements.txt             # Python dependencies
├── .env.example                 # Sample environment file
└── README.md                    # This file
```

---

## 🛠️ Dependencies

### Python Packages

- `openai`
- `jinja2`
- `python-dotenv`

Install them with:

```bash
pip install -r requirements.txt
```

### System Tools

- `pdflatex` (from TeX Live, MacTeX, or MiKTeX)
- `git` (optional, for cloning)

---

## ✏️ Customization

| To change...                        | Edit...                          |
|------------------------------------|----------------------------------|
| CV or letter layout & fonts        | `.tex` template files            |
| GPT prompt rules / tone            | Inside `generate_cv.py` or `my_cover_letter.py` |
| Number of skills shown in CV       | Line: `skills = all_skills[:6]`  |

---

## 📄 License

This project is licensed under the **MIT License**. See `LICENSE` for details.

---

## 🙏 Acknowledgements

- Powered by the [OpenAI API](https://platform.openai.com)  
- Built using [Jinja2](https://jinja.palletsprojects.com/) and [LaTeX](https://www.latex-project.org)

---

🎯 Build your best CV and cover letter — optimized for ATS, ready for humans.
