import streamlit as st
st.set_page_config(page_title="Certification Guide", layout="centered")
st.title("Certification Guide")
st.markdown("""
Use this guide to find top certifications in your domain. Each includes a link, estimated effort, and level.
""")

# --- Category Selection ---
domain = st.selectbox("Select Your Domain", [
    "Artificial Intelligence", "Web Development", "Cyber Security",
    "Data Science", "App Development", "UI/UX Design"
])

# --- Certifications Database ---
certifications = {
    "Artificial Intelligence": [
        {"title": "AI For Everyone - Andrew Ng (Coursera)",
         "url": "https://www.coursera.org/learn/ai-for-everyone",
         "level": "Beginner", "duration": "4 weeks"},
        {"title": "Deep Learning Specialization",
         "url": "https://www.coursera.org/specializations/deep-learning",
         "level": "Intermediate", "duration": "3 months"}
    ],
    "Web Development": [
        {"title": "Responsive Web Design (freeCodeCamp)",
         "url": "https://www.freecodecamp.org/learn/responsive-web-design/",
         "level": "Beginner", "duration": "5 weeks"},
        {"title": "Full Stack Developer Nanodegree (Udacity)",
         "url": "https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044",
         "level": "Advanced", "duration": "4 months"}
    ],
    "Cyber Security": [
        {"title": "Introduction to Cyber Security - NYU",
         "url": "https://www.edx.org/course/intro-to-cybersecurity",
         "level": "Beginner", "duration": "6 weeks"},
        {"title": "Google Cybersecurity Certificate",
         "url": "https://grow.google/certificates/cybersecurity/",
         "level": "Intermediate", "duration": "3 months"}
    ],
    "Data Science": [
        {"title": "IBM Data Science Professional Certificate",
         "url": "https://www.coursera.org/professional-certificates/ibm-data-science",
         "level": "Intermediate", "duration": "3 months"},
        {"title": "Python for Data Science - edX",
         "url": "https://www.edx.org/course/python-for-data-science",
         "level": "Beginner", "duration": "5 weeks"}
    ],
    "App Development": [
        {"title": "Android Basics in Kotlin (Google)",
         "url": "https://developer.android.com/courses/android-basics-kotlin/course",
         "level": "Beginner", "duration": "4-6 weeks"},
        {"title": "iOS App Development with Swift",
         "url": "https://www.edx.org/professional-certificate/ios-app-development",
         "level": "Intermediate", "duration": "2-3 months"}
    ],
    "UI/UX Design": [
        {"title": "Google UX Design Certificate",
         "url": "https://grow.google/certificates/ux-design/",
         "level": "Beginner", "duration": "4 months"},
        {"title": "UI Design with Figma (Coursera)",
         "url": "https://www.coursera.org/learn/ui-design",
         "level": "Intermediate", "duration": "4 weeks"}
    ]
}

# --- Display Certifications ---
st.subheader(f"Recommended Certifications for {domain}")

for cert in certifications.get(domain, []):
    st.markdown(f"**{cert['title']}**")
    st.markdown(f"- [Visit Course]({cert['url']})")
    st.markdown(f"- Level: `{cert['level']}`  |  Duration: `{cert['duration']}`")
    st.markdown("---")