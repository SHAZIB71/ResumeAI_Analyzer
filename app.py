import streamlit as st

from pdf_reader import extract_text_from_pdf
from analyzer import ResumeAnalyzer
from cover_letter import CoverLetterGenerator

from report_generator import (
    generate_pdf,
    generate_cover_letter_pdf
)

from charts.charts import (
    skills_chart,
    missing_skills_chart
)

from database import (
    create_database,
    save_analysis,
    get_history
)

from streamlit_extras.metric_cards import style_metric_cards
from utils.grading import grade_description
from utils.advanced_features import (
    build_resume_rewriter,
    build_interview_prep,
    build_linkedin_optimizer,
    build_email_generator,
    export_text_to_docx
)
from config import API_CONFIGURED


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="ResumeAI Analyzer Pro",
    page_icon="📄",
    layout="wide"
)


# ---------------- LOAD CSS ---------------- #

def load_css():

    try:

        with open("assets/style.css") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except Exception:

        pass


load_css()

create_database()


# ---------------- SIDEBAR ---------------- #

st.sidebar.title("📄 ResumeAI Analyzer Pro")

st.sidebar.success("🤖 Powered by Google Gemini")

st.sidebar.markdown("""
## Features

✅ ATS Resume Analysis

✅ ATS Score

✅ Resume Grade

✅ Job Match Score

✅ Resume Summary

✅ Skills Detection

✅ Missing Skills

✅ Resume Analytics

✅ AI Suggestions

✅ Cover Letter Generator

✅ Resume PDF

✅ Cover Letter PDF

✅ Resume History
""")


# ---------------- MAIN PAGE ---------------- #

st.title("📄 ResumeAI Analyzer Pro")

st.write(
    "Upload your resume and get an AI-powered ATS analysis."
)

if not API_CONFIGURED:
    st.warning(
        "⚠️ Gemini API is not configured yet. "
        "Add your GEMINI_API_KEY to your environment or .env file "
        "to enable AI analysis and cover letter generation."
    )
else:
    st.success("✅ Gemini AI is ready to analyze your resume.")


# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "🎯 Paste Job Description (Optional)",
    height=200,
    placeholder="Paste Job Description here..."
)

st.info(
    "💡 Tip: Upload a clear PDF resume and optionally paste a job description "
    "for better AI-powered matching."
)


# ---------------- COVER LETTER ---------------- #

st.divider()

st.subheader("💌 AI Cover Letter")

if uploaded_file:

    if st.button("📝 Generate Cover Letter", disabled=not API_CONFIGURED):

        with st.spinner("Generating Cover Letter..."):

            resume_text = extract_text_from_pdf(
                uploaded_file
            )

            generator = CoverLetterGenerator()

            cover_letter = generator.generate(
                resume_text,
                job_description
            )

        st.success("✅ Cover Letter Generated")

        st.text_area(
            "Generated Cover Letter",
            value=cover_letter,
            height=350
        )

        try:

            pdf_file = generate_cover_letter_pdf(
                cover_letter
            )

            with open(pdf_file, "rb") as pdf:

                st.download_button(
                    "📄 Download Cover Letter PDF",
                    data=pdf,
                    file_name="Cover_Letter.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

        except Exception as e:

            st.error(f"PDF Error : {e}")

        st.divider()


# ---------------- ANALYZE BUTTON ---------------- #

if uploaded_file:

    st.success("✅ Resume Uploaded Successfully")

    try:
        preview_text = extract_text_from_pdf(uploaded_file)
        preview = preview_text[:1200]
        if preview:
            with st.expander("📝 Preview extracted resume text"):
                st.text(preview)
    except Exception as e:
        st.warning(f"Preview unavailable: {e}")

    if st.button("🚀 Analyze Resume", disabled=not API_CONFIGURED):

        with st.spinner("Analyzing Resume..."):

            resume_text = extract_text_from_pdf(
                uploaded_file
            )

            analyzer = ResumeAnalyzer()

            result = analyzer.analyze(
                resume_text,
                job_description
            )

        st.session_state["result"] = result

        save_analysis(result)

        st.success("✅ Analysis Completed")
        # ---------------- DISPLAY RESULTS ---------------- #

if st.button("🧹 Clear Results"):
    st.session_state.pop("result", None)
    st.success("✅ Results cleared.")

if "result" in st.session_state:

    result = st.session_state["result"]

    score = result.get("ats_score", 0)

    # ---------------- ATS SCORE ---------------- #

    st.subheader("📊 ATS Score")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "ATS Score",
            f"{score}/100"
        )

    with col2:

        if score >= 80:

            st.success("Excellent Resume")

        elif score >= 60:

            st.warning("Needs Improvement")

        else:

            st.error("Low ATS Score")

    with col3:

        st.metric(
            "Status",
            "Completed"
        )

    style_metric_cards()

    st.progress(score / 100)

    st.divider()

    # ---------------- RESUME GRADE ---------------- #

    grade, status, description = grade_description(score)

    st.subheader("🏆 Resume Grade")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Grade",
            grade
        )

    with c2:

        st.metric(
            "Performance",
            status
        )

    st.info(description)

    st.divider()

    # ---------------- JOB MATCH ---------------- #

    match = result.get("job_match", 0)

    st.subheader("🎯 Job Match Score")

    st.progress(match / 100)

    st.metric(
        "Job Match",
        f"{match}%"
    )

    st.divider()

    # ---------------- SUMMARY ---------------- #

    st.subheader("📝 Resume Summary")

    st.info(
        result.get(
            "summary",
            "No summary available."
        )
    )

    st.divider()

    # ---------------- SKILLS ---------------- #

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("💻 Skills")

        skills = result.get(
            "skills",
            []
        )

        if skills:

            for skill in skills:

                st.success(skill)

        else:

            st.info(
                "No skills detected."
            )

    with col2:

        st.subheader("📚 Missing Skills")

        missing = result.get(
            "missing_skills",
            []
        )

        if missing:

            for skill in missing:

                st.error(skill)

        else:

            st.success(
                "No missing skills."
            )

    st.divider()

    # ---------------- CHARTS ---------------- #

    st.subheader("📈 Resume Analytics")

    try:

        chart = skills_chart(skills)

        if chart:

            st.plotly_chart(
                chart,
                use_container_width=True
            )

    except Exception:

        pass

    try:

        chart2 = missing_skills_chart(
            missing
        )

        if chart2:

            st.plotly_chart(
                chart2,
                use_container_width=True
            )

    except Exception:

        pass

    st.divider()

    # ---------------- STRENGTHS ---------------- #

    st.subheader("💪 Strengths")

    strengths = result.get(
        "strengths",
        []
    )

    if strengths:

        for item in strengths:

            st.success(item)

    else:

        st.info(
            "No strengths found."
        )

    # ---------------- WEAKNESSES ---------------- #

    st.subheader("⚠️ Weaknesses")

    weaknesses = result.get(
        "weaknesses",
        []
    )

    if weaknesses:

        for item in weaknesses:

            st.warning(item)

    else:

        st.success(
            "No weaknesses found."
        )

    st.divider()

    # ---------------- SUGGESTIONS ---------------- #

    st.subheader("💡 AI Suggestions")

    suggestions = result.get(
        "suggestions",
        []
    )

    if suggestions:

        for item in suggestions:

            st.write("👉", item)

    else:

        st.info(
            "No suggestions available."
        )

    st.divider()

    # ---------------- PDF DOWNLOAD ---------------- #

    st.subheader("📄 Download Resume Report")

    try:

        pdf_file = generate_pdf(result)

        with open(pdf_file, "rb") as pdf:

            st.download_button(
                label="⬇️ Download Resume Report (PDF)",
                data=pdf,
                file_name="Resume_Analysis_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    except Exception as e:

        st.error(f"PDF Generation Error: {e}")

    st.divider()

# ---------------- CAREER TOOLKIT ---------------- #

st.subheader("🧰 Career Toolkit")

if uploaded_file:
    try:
        resume_text = extract_text_from_pdf(uploaded_file)
        toolkit_tab1, toolkit_tab2, toolkit_tab3, toolkit_tab4 = st.tabs([
            "✍️ Resume Rewriter",
            "🎤 Interview Prep",
            "💼 LinkedIn Optimizer",
            "📧 Email Generator"
        ])

        with toolkit_tab1:
            rewrite = build_resume_rewriter(resume_text, job_description)
            st.write(rewrite["title"])
            st.text_area(
                "Enhanced Summary",
                value=rewrite["summary"],
                height=120
            )
            st.write("Suggested bullets:")
            for bullet in rewrite["bullets"]:
                st.write("-", bullet)

        with toolkit_tab2:
            prep = build_interview_prep(resume_text, job_description)
            st.write(prep["title"])
            for q in prep["questions"]:
                st.write("-", q)
            st.write("Tips:")
            for tip in prep["tips"]:
                st.write("-", tip)

        with toolkit_tab3:
            linkedin = build_linkedin_optimizer(resume_text, job_description)
            st.write(linkedin["headline"])
            st.text_area("About section", value=linkedin["about"], height=140)

        with toolkit_tab4:
            email = build_email_generator("Software Developer", "Your Company")
            st.text_input("Subject", value=email["subject"])
            st.text_area("Email Body", value=email["body"], height=220)

        st.divider()

        if st.button("📄 Export as DOCX"):
            docx_path = "resume_toolkit.docx"
            export_text_to_docx(resume_text[:4000], docx_path)
            with open(docx_path, "rb") as docx_file:
                st.download_button(
                    "Download DOCX",
                    data=docx_file,
                    file_name="resume_toolkit.docx",
                    mime=(
                        "application/vnd.openxmlformats-officedocument."
                        "wordprocessingml.document.main"
                    )
                )
    except Exception as e:
        st.warning(f"Career toolkit unavailable: {e}")
else:
    st.info("Upload a resume to unlock the Career Toolkit features.")

st.divider()

# ---------------- HISTORY ---------------- #

st.subheader("📜 Resume Analysis History")

history = get_history()

if history:

    for item in history:

        col1, col2, col3 = st.columns([3, 2, 2])

        with col1:
            st.write(f"📅 {item[1]}")

        with col2:
            st.write(f"ATS: {item[2]}/100")

        with col3:
            st.write(f"Match: {item[3]}%")

else:

    st.info("No analysis history found.")

st.divider()

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown(
    """
<div style="text-align:center;padding:20px;">

## 📄 ResumeAI Analyzer Pro

🤖 Powered by Google Gemini

Developed using Python • Streamlit • SQLite • ReportLab

Made with ❤️ by Shazib Huda

Version 2.0

</div>
""",
    unsafe_allow_html=True
)
