# ATS Resume Expert

 An AI-powered resume analysis tool that evaluates a candidate's resume against a specific job description and provides actionable insights for improvement.

 ## Live Demo

 **Try the ATS Resume Expert**

 ## Key Features

 - **Resume Analysis** — Reviews the resume against the target job.
- **ATS Match Score** — Provides an estimated resume-to-job match percentage.
- **Keyword Analysis** — Identifies matching and missing keywords.
- **Strengths & Gaps** — Highlights relevant skills and areas that need improvement.
- **Actionable Suggestions** — Recommends ways to make the resume more relevant and ATS-friendly.
- **PDF Support** — Analyzes uploaded PDF resumes.

 ## Technology Stack

 - Python
- Streamlit
- Google Gemini AI
- Google GenAI SDK

 ## Link of Website

 Below is the link of website:

```
https://atsresumeexpert-nnjpxrqyc7bqfbagkzsokh.streamlit.app/
```

 Install dependencies:

```
pip install -r requirements.txt
```

 Run the application:

```
streamlit run app.py
```

 ## Project Workflow

```
Resume PDF + Job Description
            ↓
       Gemini AI Analysis
            ↓
   ┌────────┴────────┐
   ↓                 ↓
Resume Review    ATS Analysis
                     ↓
          Match Score + Keywords
          + Skill Gaps + Suggestions
```

 ## Project Objective

 The goal of this project is to use Generative AI to make resume screening more transparent and help candidates **better align their resumes with specific job requirements**.

 > **Note:** The ATS score is an AI-generated estimate and is intended as a resume improvement guide, not a guarantee of selection.
