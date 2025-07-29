import streamlit as st

st.set_page_config(page_title="Resume Help", layout="centered")
st.title("Resume Guidance Assistant")
st.markdown("Build a resume that aligns with your domain, skills, and target role.")

# === Resume Structure ===
st.subheader("Resume Structure")
st.markdown("""
- **Contact Information:** Name, Phone Number, Email, LinkedIn/GitHub  
- **Objective:** A concise 1–2 line goal aligned with your domain or job  
- **Education:** Degrees, institutions, years, CGPA  
- **Skills:** Technical tools, languages, libraries  
- **Projects:** List 2–3 key academic or personal projects  
- **Experience:** Internships, part-time roles (if any)  
- **Certifications:** Only relevant to the domain  
- **Extras:** Volunteering, positions of responsibility  
""")

# === Objective Section ===
st.subheader("What to Write in Objective?")
objective_mode = st.radio("How do you want to generate your objective?", ["By Domain", "By Job Description"])

# --- Option 1: By Domain ---
objective_templates = {
    "Data Science": "Aspiring data scientist skilled in Python, statistics, and machine learning, seeking to leverage data insights for real-world problems.",
    "AI/ML": "Motivated learner in AI/ML, aiming to build scalable intelligent systems using cutting-edge models and frameworks.",
    "Web Development": "Frontend and backend web developer eager to create interactive, responsive, and scalable web applications.",
    "Cyber Security": "Cybersecurity enthusiast looking to apply ethical hacking and defense techniques to protect digital infrastructure.",
    "App Development": "Mobile app developer passionate about building intuitive applications using Flutter/Kotlin.",
    "UI/UX": "Creative UI/UX designer focused on enhancing user experience through minimal and meaningful interfaces.",
    "General": "Detail-oriented student enthusiastic about applying skills in real-world industry projects and gaining hands-on experience."
}

if objective_mode == "By Domain":
    selected_domain = st.selectbox("Select Your Domain", list(objective_templates.keys()))
    st.markdown("**Suggested Objective:**")
    st.text_area("Generated Objective", value=objective_templates[selected_domain], height=80)

# --- Option 2: By Job Description ---
else:
    job_desc = st.text_area("Paste the Job Description Below", height=150)
    generated_objective = ""
    if st.button("Generate Objective"):
        # Placeholder logic
        generated_objective = (
            "Results-oriented candidate aiming to apply my skills in alignment with the job requirements stated, "
            "including Python, SQL, and data analytics."
        )

    if generated_objective:
        st.markdown("**Generated Objective (ATS-friendly):**")
        st.text_area("Generated Objective", value=generated_objective, height=80)

# === Skill Keywords ===
st.subheader("Skills to Include")
selected_skills = st.multiselect("Select your known skills", [
    "Python", "Java", "SQL", "React", "Machine Learning", "HTML", "CSS", "JavaScript", 
    "MongoDB", "Linux", "Figma", "Kotlin", "Flutter", "Power BI"
])
if selected_skills:
    st.success("Include these in your Skills section:\n" + ", ".join(selected_skills))

# === Project Suggestions ===
st.subheader("Suggested Projects Based on Your Domain & Skills")

project_suggestions = {
    "Data Science": {
        "Python": ["Fake News Detection", "EDA on COVID Dataset"],
        "SQL": ["Sales Data Analysis Dashboard", "Employee Attrition Analysis"],
        "Power BI": ["Interactive Sales Insights"],
    },
    "Web Development": {
        "HTML": ["Personal Portfolio Site", "Responsive Blog Website"],
        "JavaScript": ["Todo App", "Weather App"],
        "React": ["Movie Booking UI", "Dashboard with Auth"],
    },
    "Cyber Security": {
        "Linux": ["Port Scanner", "Log File Analyzer"],
        "Python": ["Keylogger Tracker", "Phishing URL Detector"]
    },
    "App Development": {
        "Flutter": ["Expense Tracker", "Fitness App UI"],
        "Kotlin": ["Note Taking App", "Simple Alarm Clock"]
    },
    "UI/UX": {
        "Figma": ["Redesign Food Delivery App", "E-commerce UX Mockup"]
    },
    "AI/ML": {
        "Machine Learning": ["Handwritten Digit Recognition", "Spam Classifier"],
        "Python": ["Chatbot using RNN", "Stock Price Predictor"]
    }
}

if selected_skills:
    shown_projects = set()
    for skill in selected_skills:
        for domain, mapping in project_suggestions.items():
            if skill in mapping:
                for proj in mapping[skill]:
                    shown_projects.add(f"- {proj}")
    if shown_projects:
        st.markdown("\n".join(sorted(shown_projects)))
    else:
        st.info("No specific project suggestions for selected skills. Try adding more technical skills.")
else:
    st.info("Please select your skills to see relevant project ideas.")


st.subheader("Recommended Resume Builders")

st.markdown("""
Build your resume easily using trusted online tools:

- [Canva Resume Builder](https://www.canva.com/resumes/) – Professionally designed templates with drag-and-drop editing.
- [Novoresume](https://novoresume.com/) – ATS-friendly templates tailored for freshers and professionals.
- [Zety](https://zety.com/resume-builder) – Smart guided resume builder with content suggestions.
- [Kickresume](https://www.kickresume.com/) – AI-powered builder with customization options.
- [ResumeGenius](https://resumegenius.com/resume-builder) – Fast resume creation with expert-approved templates.
- [Google Docs Resume Templates](https://docs.google.com/document/u/0/) – Free, accessible templates under “Template Gallery”.
""")