from config import client, MODEL


def generate_cover_letter(
    resume_text,
    job_description,
    company_name,
    job_title
):
    """
    Generate a personalized cover letter using Gemini.
    """

    if not resume_text.strip():
        return "Please provide resume content."

    if not job_description.strip():
        return "Please provide the job description."

    if not company_name.strip():
        return "Please enter the company name."

    if not job_title.strip():
        return "Please enter the job title."

    prompt = f"""
    You are an expert career advisor and professional cover letter writer.

    Generate a personalized cover letter using the candidate's
    resume and the target job description.

    CANDIDATE RESUME:
    {resume_text}

    JOB DESCRIPTION:
    {job_description}

    COMPANY NAME:
    {company_name}

    JOB TITLE:
    {job_title}

    INSTRUCTIONS:

    1. Address the letter to the hiring team.
    2. Introduce the candidate and mention the job title.
    3. Explain why the candidate is interested in the position.
    4. Highlight relevant technical skills from the resume.
    5. Include relevant projects and practical experience.
    6. Connect the candidate's actual experience to the job requirements.
    7. Explain how the candidate could contribute to the company.
    8. Maintain a professional and confident tone.
    9. Keep the letter concise, approximately 250-350 words.
    10. Do not invent qualifications, achievements, or experience.
    11. Do not claim professional experience when the candidate has only demonstrated a skill through projects.
    12. Avoid generic statements and unnecessary exaggeration.
    12. Every technical claim must be directly supported by the candidate's resume.
    13. Do not use words such as "expert", "extensive experience", or "proven professional experience" unless explicitly supported by the resume.
    14. Distinguish between professional work experience, academic projects, and personal projects.
    15. Do not claim that a project was deployed unless the resume explicitly confirms its deployment.
    16. Prioritize the most relevant experience instead of mentioning every skill or project.

    OUTPUT FORMAT:

    Professional Cover Letter

    Dear Hiring Team,

    [Cover letter content]

    Sincerely,
    [Candidate Name]
    """

    try:
        response = client.interactions.create(
            model=MODEL,
            input=prompt
        )

        return response.output_text

    except Exception as e:
        return f"Error generating cover letter: {str(e)}"