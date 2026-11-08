from config import client, MODEL


def enhance_resume(resume_text, job_description=""):
    """
    Improve a resume using Gemini AI.

    Args:
        resume_text: Extracted text from the uploaded resume.
        job_description: Optional job description for tailoring.

    Returns:
        AI-enhanced resume content.
    """

    if not resume_text.strip():
        return "Please provide valid resume content."

    prompt = f"""
    You are an expert technical recruiter and ATS resume specialist.

    Your task is to analyze a candidate's resume against a job
    description and generate a tailored resume.

    IMPORTANT RULES:
    1. Never invent qualifications, skills, experience or achievements.
    2. Never add technologies simply because they appear in the JD.
    3. Preserve the candidate's original employment history and dates.
    4. Do not change completed education into ongoing education.
    5. Improve wording without exaggerating responsibilities.
    6. Prioritize relevant technical skills and projects.
    7. Use professional, ATS-friendly formatting.
    8. Keep the resume suitable for the candidate's actual experience level.

    PART 1: TAILORED RESUME

    Generate a revised resume containing:
    - Professional Summary
    - Technical Skills
    - Relevant Projects
    - Professional Experience
    - Education
    - Certifications

    PART 2: JOB DESCRIPTION ANALYSIS

    After the resume, provide:

    1. MATCHING SKILLS:
    Skills from the candidate's resume that match the JD.

    2. MISSING SKILLS:
    JD requirements not demonstrated in the resume.
    Do not assume the candidate lacks a skill just because
    it is not mentioned. Label these as "Not demonstrated".

    3. RELEVANT PROJECTS:
    Explain which projects best demonstrate suitability
    for the position.

    4. IMPROVEMENT SUGGESTIONS:
    Recommend practical skills or topics the candidate
    should learn to become a stronger applicant.

    5. INTERVIEW PREPARATION:
    Suggest five technical questions based on the JD
    and the candidate's projects.

    JOB DESCRIPTION:
    {job_description}

    ORIGINAL RESUME:
    {resume_text}
    """

    try:
        response = client.interactions.create(
            model=MODEL,
            input=prompt
        )

        return response.output_text

    except Exception as e:
        return f"Error enhancing resume: {str(e)}"