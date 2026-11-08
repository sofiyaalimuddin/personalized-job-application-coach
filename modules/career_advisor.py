from config import client, MODEL


def get_career_advice(resume_text, job_description):

    if not resume_text.strip():
        return "Please provide valid resume content."

    if not job_description.strip():
        return "Please provide the job description."

    prompt = f"""
    You are an experienced career advisor and technical recruiter.

    Analyze the candidate's resume against the target job description.
    Provide practical, personalized career and job application advice.

    CANDIDATE RESUME:
    {resume_text}

    TARGET JOB DESCRIPTION:
    {job_description}

    Provide your response using the following sections:

    1. CANDIDATE PROFILE
    - Briefly summarize the candidate's current skills,
      experience, education, and project background.
    - Identify the candidate's strongest areas.

    2. SKILL GAP ANALYSIS
    - Identify skills demonstrated in the resume that match
      the job requirements.
    - Identify important job requirements that are not
      demonstrated in the resume.
    - Distinguish between missing evidence and confirmed
      lack of a skill.
    - Prioritize the most important gaps.

    3. CAREER RECOMMENDATIONS
    - Explain how well the candidate's background aligns
      with the target position.
    - Suggest up to three relevant job roles the candidate
      could realistically consider.
    - Prioritize entry-level opportunities when appropriate.
    - Explain why each suggested role is relevant.

    4. PERSONALIZED LEARNING ROADMAP
    - Recommend the most important skills to learn next.
    - Divide the roadmap into:
      Immediate Priorities
      Short-Term Learning
      Long-Term Development
    - Explain why each recommended skill matters.
    - Avoid recommending skills that the candidate
      has already demonstrated without a clear reason.

    5. INTERVIEW PREPARATION
    - Generate five technical or role-related interview
      questions based on the job description.
    - Include two questions based on the candidate's
      actual projects or work experience.
    - Suggest the main points the candidate should cover
      when answering.

    6. JOB APPLICATION STRATEGY
    - Recommend which projects and experiences to highlight.
    - Suggest improvements to the resume for this position.
    - Identify potential concerns a recruiter might have.
    - Give practical suggestions to improve the application.

    7. FINAL CAREER ADVICE
    - Give an honest assessment of the candidate's
      current preparation.
    - Identify the three most important next actions.
    - Keep recommendations realistic and actionable.

    IMPORTANT RULES:
    - Base all candidate-specific claims on the supplied resume.
    - Never invent qualifications, skills, experience,
      achievements, or project features.
    - Do not assume a candidate lacks a skill simply because
      it is not mentioned in the resume.
    - Clearly distinguish professional experience from
      personal or academic projects.
    - Do not exaggerate the candidate's suitability.
    - Do not provide arbitrary ATS scores or percentages.
    - Avoid generic motivational advice.
    - Prioritize practical recommendations for an
      entry-level candidate.
    - Never attribute a technology to a professional role
      unless the resume explicitly confirms its use in that role.
    - Distinguish Google Apps Script automation from
      Python development experience.
    - Do not assume that GitHub or deployment experience
      is missing without checking the complete resume.
    - Do not make comparisons between the candidate
      and other job applicants.
    - Separate job-specific skill gaps from general
      professional development recommendations.
    - Prioritize learning recommendations according
      to their relevance to the target job.
    - Do not recommend learning a technology merely
      because it is popular.
    - Consider the candidate's existing projects and
      demonstrated skills before recommending new projects.

    Use clear headings, bullet points, and concise explanations.
    """

    try:
        response = client.interactions.create(
            model=MODEL,
            input=prompt
        )

        return response.output_text

    except Exception as e:
        return f"Error generating career advice: {str(e)}"