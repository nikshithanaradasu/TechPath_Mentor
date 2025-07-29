import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="Resume Builder", layout="centered")

st.title("Resume Builder")
st.markdown("Fill in your details to generate a professional resume.")

with st.form("resume_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    linkedin = st.text_input("LinkedIn URL")
    github = st.text_input("GitHub URL")

    summary = st.text_area("Professional Summary")

    skills = st.text_area("Skills (comma-separated)")
    education = st.text_area("Education (include Degree, Institution, Year)")
    projects = st.text_area("Projects (title and short description)")
    experience = st.text_area("Work Experience (optional)")

    submitted = st.form_submit_button("Generate Resume")

# PDF Generation Function
def create_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, data["name"], ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 8, f"Email: {data['email']} | Phone: {data['phone']}", ln=True, align='C')
    if data["linkedin"] or data["github"]:
        pdf.cell(200, 8, f"LinkedIn: {data['linkedin']} | GitHub: {data['github']}", ln=True, align='C')

    pdf.ln(10)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Professional Summary", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, data["summary"])

    pdf.ln(4)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, data["skills"])

    pdf.ln(4)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Education", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, data["education"])

    pdf.ln(4)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Projects", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, data["projects"])

    if data["experience"]:
        pdf.ln(4)
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, "Work Experience", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 8, data["experience"])

    return pdf

# Generate and download
if submitted and name and email:
    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "linkedin": linkedin,
        "github": github,
        "summary": summary,
        "skills": skills,
        "education": education,
        "projects": projects,
        "experience": experience,
    }

    pdf = create_pdf(data)
    pdf_output = f"{name.replace(' ', '_')}_Resume.pdf"
    pdf.output(pdf_output)

    with open(pdf_output, "rb") as f:
        st.success("Resume generated successfully!")
        st.download_button("Download Resume", f, file_name=pdf_output, mime="application/pdf")