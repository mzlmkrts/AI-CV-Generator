# AI-Powered CV & Cover-Letter Generator

A command-line tool that takes your **`profile.json`** and a job description, uses the OpenAI API to optimise your CV for Applicant Tracking Systems (ATS), renders a LaTeX template, and outputs a high-quality PDF résumé.

---

## 🔍 Features

- **Strict mode** – exact ATS-friendly wording (no new content)  
- **Creative mode** – human-friendly rewording **plus** ATS optimisation  
- Automatically highlights your **top 6 most relevant skills**  
- Professional, fully customisable **LaTeX** styling → polished PDF output  
- Clean, prompt-driven **CLI** workflow

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
   Then open `.env` in a text editor and set:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install LaTeX (`pdflatex`)**

   You need a working LaTeX installation. Here’s how to install it:

   - **Ubuntu / Debian**
     ```bash
     sudo apt update
     sudo apt install texlive-latex-base texlive-fonts-recommended texlive-latex-extra
     ```

   - **macOS (with Homebrew)**
     ```bash
     brew install --cask mactex-no-gui
     ```

   - **Windows**
     Download and install [MiKTeX](https://miktex.org/download)

5. **Prepare your input files**

   - `profile.json` — your personal data, education, experience, skills, etc.  
   - `job_description.txt` — plain text job advertisement or description

6. **Run the generator**

   ```bash
   python generate_cv.py
   ```

   When prompted, choose a generation mode:
   ```
   Which mode do you want to use? (strict/creative):
   ```

7. **View the output**

   Your generated CV will be saved as:
   ```
   generated_cv.pdf
   ```

---

## ⚙️ Project Structure

```
.
├── generate_cv.py            # Main script
├── modern_cv_template.tex    # Jinja2-powered LaTeX template
├── profile.json              # Example user profile
├── job_description.txt       # Example job description
├── requirements.txt          # Python dependencies
├── .env.example              # Template for API key
└── README.md                 # This file
```

---

## 🛠️ Dependencies

### Python packages

- `openai`
- `jinja2`
- `python-dotenv`

Install with:

```bash
pip install -r requirements.txt
```

### System tools

- `pdflatex` (LaTeX engine for compiling PDFs)
- `git` (for cloning and version control)

---

## ✏️ Customization

| To change...                     | Edit...                       |
|----------------------------------|-------------------------------|
| Layout / fonts / styling         | `modern_cv_template.tex`      |
| GPT prompt logic and behavior    | `generate_cv.py`              |
| Number of displayed skills       | Slice line: `skills = all_skills[:6]` |

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 🙏 Acknowledgements

- Powered by the [OpenAI API](https://platform.openai.com)
- Built with [Jinja2](https://jinja.palletsprojects.com/) and [LaTeX](https://www.latex-project.org)

Happy résumé-building! 🚀
