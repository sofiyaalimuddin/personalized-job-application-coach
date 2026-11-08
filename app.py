import gradio as gr

from utils.document_parser import extract_text_from_pdf
from modules.resume_enhancer import enhance_resume
from modules.cover_letter import generate_cover_letter
from modules.career_advisor import get_career_advice

from utils.document_parser import extract_resume_text


def get_resume_text(file_path):

    if file_path is None:
        return None, "Please upload your resume."

    resume_text = extract_resume_text(file_path)

    if resume_text.startswith("Error:"):
        return None, resume_text

    return resume_text, None


def process_resume(pdf_file, job_description):
    """Enhance the resume according to the job description."""

    if not job_description.strip():
        return "Please enter the job description."

    resume_text, error = get_resume_text(pdf_file)

    if error:
        return error

    return enhance_resume(resume_text, job_description)


def process_cover_letter(pdf_file, job_description, company_name, job_title):
    """Generate a personalized cover letter."""

    if not job_description.strip():
        return "Please enter the job description."

    resume_text, error = get_resume_text(pdf_file)

    if error:
        return error

    return generate_cover_letter(
        resume_text,
        job_description,
        company_name,
        job_title
    )

def process_career_advice(pdf_file, job_description):

    if not job_description.strip():
        return "Please enter the job description."

    resume_text, error = get_resume_text(pdf_file)

    if error:
        return error

    return get_career_advice(
        resume_text,
        job_description
    )

with gr.Blocks(title="AI Job Application Coach") as demo:

    gr.Markdown("""
    # AI Job Application Coach

    ### Your AI-powered assistant for personalized job applications.

    Upload your resume and paste a job description to get started.
    """)

    # Shared inputs
    gr.Markdown("## 1. Candidate Information")

    resume_file = gr.File(
        label="Upload Your Resume",
        file_types=[".pdf", ".docx", ".txt"],
        file_count="single",
        type="filepath"
    )

    job_description = gr.Textbox(
        label="Target Job Description",
        placeholder="Paste the complete job description here...",
        lines=8
    )

    # Application tools
    gr.Markdown("## 2. Application Tools")

    with gr.Tabs():

        # Resume Enhancer Tab
        with gr.Tab("Resume Enhancer"):

            gr.Markdown("""
            ### AI Resume Enhancer

            Improve your resume and identify how well your
            existing skills and projects match the job requirements.
            """)

            enhance_button = gr.Button(
                "Enhance My Resume",
                variant="primary"
            )

            resume_output = gr.Textbox(
                label="Enhanced Resume & Job Analysis",
                lines=25,
                interactive=False
            )

            enhance_button.click(
                fn=process_resume,
                inputs=[resume_file, job_description],
                outputs=resume_output
            )

        # Cover Letter Generator Tab
        with gr.Tab("Cover Letter Generator"):

            gr.Markdown("""
            ### Personalized Cover Letter Generator

            Generate a professional cover letter based on your
            resume and the target job description.
            """)

            company_name = gr.Textbox(
                label="Company Name",
                placeholder="Enter company name..."
            )

            job_title = gr.Textbox(
                label="Job Title",
                placeholder="Enter job title..."
            )

            cover_letter_button = gr.Button(
                "Generate Cover Letter",
                variant="primary"
            )

            cover_letter_output = gr.Textbox(
                label="Generated Cover Letter",
                lines=18,
                interactive=False
            )

            cover_letter_button.click(
                fn=process_cover_letter,
                inputs=[
                    resume_file,
                    job_description,
                    company_name,
                    job_title
                ],
                outputs=cover_letter_output
            )

        # Career Advisor Tab
                # Career Advisor Tab
        with gr.Tab("Career Advice"):

            gr.Markdown("""
            ### AI Career Advisor

            Get personalized career recommendations,
            identify skill gaps, prepare for interviews,
            and build a practical learning roadmap.
            """)

            advice_button = gr.Button(
                "Get Career Advice",
                variant="primary"
            )

            advice_output = gr.Textbox(
                label="Personalized Career Recommendations",
                lines=30,
                interactive=False
            )

            advice_button.click(
                fn=process_career_advice,
                inputs=[
                    resume_file,
                    job_description
                ],
                outputs=advice_output
            )


if __name__ == "__main__":
    demo.launch()