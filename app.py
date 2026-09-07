import os

import streamlit as st
from dotenv import load_dotenv
from google import genai


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# ============================================================
# CHECK API KEY
# ============================================================

if not GOOGLE_API_KEY:
    st.error(
        "GOOGLE_API_KEY was not found. "
        "Please check your .env file."
    )
    st.stop()


# ============================================================
# INITIALIZE GEMINI
# ============================================================

client = genai.Client(api_key=GOOGLE_API_KEY)

MODEL_NAME = "gemini-2.5-flash"


# ============================================================
# GEMINI FUNCTION
# ============================================================

def get_gemini_response(pdf_file, job_description, prompt):

    try:
        # Reset file position
        pdf_file.seek(0)

        # Upload PDF to Gemini
        uploaded_pdf = client.files.upload(
            file=pdf_file,
            config={
                "mime_type": "application/pdf"
            }
        )

        # Send PDF + job description + instructions
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[
                uploaded_pdf,
                prompt,
                f"""
JOB DESCRIPTION:

{job_description}
"""
            ]
        )

        return response.text

    except Exception as e:
        return f"Error while communicating with Gemini:\n\n{str(e)}"


# ============================================================
# STREAMLIT PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ATS Resume Expert",
    page_icon="📄",
    layout="centered"
)


# ============================================================
# TITLE
# ============================================================

st.title("📄 ATS Resume Expert")

st.write(
    "Analyze your resume against a job description "
    "using Google Gemini."
)


# ============================================================
# JOB DESCRIPTION
# ============================================================

input_text = st.text_area(
    "Job Description:",
    height=250,
    placeholder="Paste the job description here..."
)


# ============================================================
# RESUME UPLOAD
# ============================================================

uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success(
        f"Resume uploaded successfully: {uploaded_file.name}"
    )


# ============================================================
# PROMPT 1 - RESUME REVIEW
# ============================================================

input_prompt1 = """
You are an experienced Technical Human Resource Manager.

Your task is to review the provided resume against the
provided job description.

Give a professional evaluation of whether the candidate's
profile aligns with the role.

Please analyze the following:

1. Overall suitability for the position
2. Candidate strengths
3. Candidate weaknesses
4. Relevant technical skills
5. Relevant work experience
6. Education and certifications
7. Important missing requirements
8. Recommendations for improving the resume

Be specific and professional.

Only use information actually present in the resume
and job description.

Do not invent skills, experience, qualifications,
projects, or achievements.
"""


# ============================================================
# PROMPT 2 - ATS MATCH
# ============================================================

input_prompt3 = """
You are an expert Applicant Tracking System (ATS) analyzer.

Your task is to compare the provided resume against
the provided job description.

Analyze the resume as an ATS would.

Return the result using exactly the following sections:

## ATS Match Percentage

Give an estimated match percentage from 0% to 100%.

Consider:
- Required technical skills
- Preferred technical skills
- Years and type of experience
- Education
- Certifications
- Job responsibilities
- Important keywords
- Tools and technologies

## Matching Keywords

List the important keywords, skills, technologies,
qualifications, and requirements from the job description
that are present in the resume.

## Missing Keywords

List important keywords, skills, technologies,
qualifications, and requirements from the job description
that are missing from the resume.

## Strengths

Explain the strongest matches between the resume
and the job description.

## Weaknesses

Explain the most important gaps between the resume
and the job description.

## Final Thoughts

Give a concise professional assessment of how well
the resume matches the job.

Also provide practical recommendations for improving
the resume.

Do not invent information that is not present
in the resume or job description.
"""


# ============================================================
# BUTTONS
# ============================================================

col1, col2 = st.columns(2)

with col1:
    submit1 = st.button(
        "🔍 Review Resume",
        use_container_width=True
    )

with col2:
    submit3 = st.button(
        "📊 ATS Match",
        use_container_width=True
    )


# ============================================================
# REVIEW RESUME
# ============================================================

if submit1:

    if uploaded_file is None:
        st.warning("Please upload your resume first.")

    elif not input_text.strip():
        st.warning("Please enter the job description first.")

    else:

        with st.spinner("Analyzing your resume..."):

            response = get_gemini_response(
                uploaded_file,
                input_text,
                input_prompt1
            )

        st.subheader("Resume Evaluation")

        st.write(response)


# ============================================================
# ATS MATCH
# ============================================================

elif submit3:

    if uploaded_file is None:
        st.warning("Please upload your resume first.")

    elif not input_text.strip():
        st.warning("Please enter the job description first.")

    else:

        with st.spinner("Calculating ATS match..."):

            response = get_gemini_response(
                uploaded_file,
                input_text,
                input_prompt3
            )

        st.subheader("ATS Analysis")

        st.write(response)
