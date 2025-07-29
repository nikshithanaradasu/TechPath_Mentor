import streamlit as st
from fpdf import FPDF
import base64
from career_mapper import generate_career_advice

st.set_page_config(page_title="Career Suggestions", layout="centered")
st.title("Career Suggestions")

# --- PDF Utility ---
def text_to_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)
    return pdf.output(dest='S').encode('latin1')

# --- Form Input ---
with st.form("career_form"):
    name = st.text_input("Your Name")

    degree = st.selectbox("Your Current Education Level", [
        "High School", "Diploma", "B.Tech", "Graduate", "Postgraduate"
    ])

    domain = st.selectbox("Preferred Domain", [
        "Artificial Intelligence", "Web Development", "Cyber Security",
        "Data Science", "App Development", "UI/UX Design"
    ])

    selected_skills = st.multiselect("Your Known Skills", [
        "Python", "Java", "C++", "SQL", "Machine Learning", "Frontend",
        "Backend", "Data Visualization", "Cloud Computing",
        "Cybersecurity Basics", "Linux", "Figma"
    ])

    other_skills_input = st.text_input("Other Skills (comma-separated)")
    other_skills = [s.strip() for s in other_skills_input.split(",")] if other_skills_input else []

    enable_download = st.checkbox("Download this suggestion as a PDF")

    submitted = st.form_submit_button("Get Suggestions")

# --- Output ---
if submitted:
    if not name.strip() or not selected_skills:
        st.warning("Please fill all required fields: Name and at least one skill.")
    else:
        suggestion = generate_career_advice(name, degree, domain, selected_skills, other_skills)

        st.subheader("Career Guidance")
        st.markdown(suggestion)

        if enable_download:
            pdf_bytes = text_to_pdf(suggestion)
            b64_pdf = base64.b64encode(pdf_bytes).decode()
            pdf_filename = f"{name.replace(' ', '_')}_career_advice.pdf"
            st.markdown(
                f'<a href="data:application/pdf;base64,{b64_pdf}" download="{pdf_filename}">📄 Download PDF Report</a>',
                unsafe_allow_html=True
            )