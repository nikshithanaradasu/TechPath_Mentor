import streamlit as st

st.set_page_config(page_title="TechPath Mentor", layout="centered")

# Adaptive Styling (no fixed colors)
st.markdown("""
<style>
.stApp {
    font-family: 'Segoe UI', sans-serif;
    padding: 1rem;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 20px;
}

/* Description */
.description {
    text-align: center;
    font-size: 18px;
    max-width: 700px;
    margin: 0 auto 40px auto;
    line-height: 1.6;
}

/* Cards */
.card {
    background-color: rgba(250, 250, 250, 0.75);
    padding: 25px 30px;
    border-radius: 10px;
    border: 1px solid var(--secondary-background-color);
    margin: 0 auto 30px auto;
    max-width: 800px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}
.card:hover {
    transform: scale(1.02);
    box-shadow: 0 4px 12px rgba(0,0,0,0.12);
}
.card h4 {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 12px;
}
.card ul, .card p {
    font-size: 16px;
    line-height: 1.7;
}

/* Footer */
.footer {
    margin-top: 60px;
    text-align: center;
    font-size: 13px;
    opacity: 0.6;
}
</style>
""", unsafe_allow_html=True)

# Page Content
st.markdown("<div class='main-title'>TechPath Mentor</div>", unsafe_allow_html=True)

st.markdown("""
<div class='description'>
Welcome to <strong>TechPath Mentor</strong> — your personalized guide to navigating tech career choices.  
This tool helps students, graduates, and professionals discover career paths based on their  
<strong>skills</strong>, <strong>education</strong>, and <strong>interests</strong>.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h4>What You Can Explore</h4>
    <ul>
        <li>Career suggestions tailored to your profile</li>
        <li>Interactive learning roadmaps</li>
        <li>Resume building tips & templates</li>
        <li>Certification & course guidance</li>
        <li>Project ideas with GitHub links</li>
    </ul>
</div>

<div class="card">
    <h4>Get Started</h4>
    <p>Use the sidebar to access various tools and sections of the platform.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='footer'>Built AIML Project for Elevate Labs | © 2025 TechPath Mentor</div>", unsafe_allow_html=True)