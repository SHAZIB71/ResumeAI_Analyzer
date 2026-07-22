import streamlit as st

from pdf_reader import extract_text_from_pdf
from analyzer import ResumeAnalyzer
from report_generator import create_report


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="ResumeAI Analyzer",
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
    except:
        pass


load_css()


# ---------------- SIDEBAR ---------------- #

st.sidebar.title("📄 ResumeAI Analyzer")

st.sidebar.success("🤖 Powered by Google Gemini")

st.sidebar.markdown("""
### Features

✅ ATS Score

✅ Job Match Score

✅ Resume Summary

✅ Skills Detection

✅ Strengths

✅ Weaknesses

✅ Missing Skills

✅ AI Suggestions

✅ Download Report
""")


# ---------------- TITLE ---------------- #

st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and compare it with a Job Description using AI."
)


# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)


# ---------------- JOB DESCRIPTION ---------------- #

job_description = st.text_area(
    "🎯 Paste Job Description (Optional)",
    height=180,
    placeholder="Paste the company's job description here..."
)


# ---------------- ANALYZE BUTTON ---------------- #

if uploaded_file:

    st.success("✅ Resume Uploaded Successfully")

    if st.button("🚀 Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            resume_text = extract_text_from_pdf(uploaded_file)

            analyzer = ResumeAnalyzer()

            result = analyzer.analyze(
                resume_text,
                job_description
            )

        st.success("✅ Analysis Completed!")

        # ---------------- SCORE SECTION ---------------- #

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "📊 ATS Score",
                f'{result["ats_score"]}/100'
            )

            st.progress(result["ats_score"] / 100)

        with col2:

            st.metric(
                "🎯 Job Match",
                f'{result.get("job_match",0)}%'
            )

            st.progress(result.get("job_match",0) / 100)

        st.divider()

        # ---------------- SUMMARY ---------------- #

        if result.get("summary"):

            st.subheader("📝 Resume Summary")

            st.success(result["summary"])

            st.divider()

        # ---------------- SKILLS ---------------- #

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("💻 Skills")

            skills = result.get("skills", [])

            if skills:

                cols = st.columns(2)

                for i, skill in enumerate(skills):

                    cols[i % 2].success(skill)

        with col2:

            st.subheader("📚 Missing Skills")

            missing = result.get("missing_skills", [])

            for skill in missing:

                st.error(skill)

        st.divider()

        # ---------------- STRENGTHS ---------------- #

        st.subheader("💪 Strengths")

        for item in result.get("strengths", []):

            st.info(item)

        # ---------------- WEAKNESSES ---------------- #

        st.subheader("⚠️ Weaknesses")

        for item in result.get("weaknesses", []):

            st.warning(item)

        st.divider()

        # ---------------- SUGGESTIONS ---------------- #

        st.subheader("💡 Suggestions")

        for item in result.get("suggestions", []):

            st.write("👉", item)

        st.divider()

        # ---------------- DOWNLOAD REPORT ---------------- #

        report = create_report(result)

        st.download_button(
            label="📥 Download Analysis Report",
            data=report,
            file_name="Resume_Analysis_Report.txt",
            mime="text/plain"
        )