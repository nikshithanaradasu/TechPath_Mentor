import streamlit as st
# Dictionary of project ideas
project_ideas = {
    "Artificial Intelligence": {
        "Beginner": [
            "AI Chatbot using rule-based logic",
            "Movie Recommendation System (basic ML)",
            "Spam Mail Classifier"
        ],
        "Intermediate": [
            "AI Virtual Assistant using NLP",
            "Facial Emotion Detection",
            "Fake News Detection with Web Scraping"
        ],
        "Advanced": [
            "Autonomous Vehicle Simulation",
            "AI-powered Career Counselor",
            "Multi-label Image Classification using Deep Learning"
        ]
    },
    "Web Development": {
        "Beginner": [
            "Personal Portfolio Website",
            "Basic Blog Website with HTML/CSS",
            "To-Do List App using JavaScript"
        ],
        "Intermediate": [
            "E-commerce Web App with Django/Flask",
            "Authentication System with JWT",
            "News Aggregator App with APIs"
        ],
        "Advanced": [
            "Full-stack Social Media Platform",
            "Real-time Chat Application using WebSockets",
            "Microservices-based SaaS Platform"
        ]
    },
    "Data Science": {
        "Beginner": [
            "Exploratory Data Analysis on Titanic Dataset",
            "COVID-19 Data Visualization Dashboard",
            "Basic Salary Prediction"
        ],
        "Intermediate": [
            "Sales Forecasting using ARIMA",
            "Customer Segmentation using Clustering",
            "Loan Approval Prediction"
        ],
        "Advanced": [
            "End-to-End ML Pipeline with CI/CD",
            "Big Data Analysis using PySpark",
            "Time Series Forecasting with LSTM"
        ]
    },
    "Cyber Security": {
        "Beginner": [
            "Password Strength Checker",
            "Basic Port Scanner using Python",
            "Secure Login Interface"
        ],
        "Intermediate": [
            "Keylogger with Security Measures",
            "Network Packet Analyzer",
            "Brute-force Attack Simulator"
        ],
        "Advanced": [
            "Intrusion Detection System",
            "Blockchain-based Authentication",
            "End-to-End Encrypted Chat App"
        ]
    }
}

# GitHub Best Practices Tips
best_practices = [
    "Use meaningful commit messages.",
    "Maintain a clear README with project overview, tech stack, and setup instructions.",
    "Organize code into modular folders (e.g., `src/`, `assets/`, `data/`).",
    "Include screenshots or demo videos.",
    "Use `.gitignore` to exclude unnecessary files.",
    "Add open-source license if sharing publicly."
]

# UI
st.title("Project Ideas and GitHub Showcase")

st.markdown("Select your domain and experience level to explore relevant project ideas.")

domain = st.selectbox("Choose a Domain", list(project_ideas.keys()))
level = st.radio("Select Experience Level", ["Beginner", "Intermediate", "Advanced"])

st.subheader("Suggested Project Ideas")

for i, idea in enumerate(project_ideas[domain][level], 1):
    st.markdown(f"{i}. {idea}")

st.markdown("---")
st.subheader("How to Present Projects on GitHub")

for tip in best_practices:
    st.markdown(f"- {tip}")

st.markdown("Looking to host your project? Check out:")
st.markdown("[GitHub Docs - Getting Started](https://docs.github.com/en/get-started)")
st.markdown("[Free GitHub Student Pack](https://education.github.com/pack)")