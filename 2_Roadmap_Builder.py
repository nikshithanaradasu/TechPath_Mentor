import streamlit as st

st.set_page_config(page_title="Roadmap Builder", layout="centered")

st.title("Learning Roadmap Builder")
st.markdown("Get a personalized roadmap tailored to your domain and learning level.")

# Select Domain and Track Level
domain = st.selectbox("Select Your Domain", [
    "Data Science", "Artificial Intelligence", "Web Development",
    "Cyber Security", "App Development", "UI/UX Design"
])

track = st.selectbox("Select Your Current Level", ["Beginner", "Intermediate", "Advanced"])

# Roadmaps with descriptions and YouTube links
roadmaps = {
    "Data Science": {
        "Beginner": {
            "note": "Start with the basics and build strong Python and math foundations.",
            "steps": [
                ("Learn Python fundamentals", "https://www.youtube.com/watch?v=_uQrJ0TkZlc"),
                ("Understand NumPy and Pandas", "https://www.youtube.com/watch?v=vmEHCJofslg"),
                ("Study basic statistics & probability", "https://www.youtube.com/watch?v=xxpc-HPKN28"),
                ("Intro to data visualization using Matplotlib/Seaborn", "https://www.youtube.com/watch?v=0D9Nnu3JgPY"),
                ("Work on beginner-level datasets from Kaggle", "https://www.kaggle.com/datasets")
            ]
        },
        "Intermediate": {
            "note": "If you're comfortable with Python and data handling, start applying ML techniques.",
            "revise": "https://www.youtube.com/watch?v=Gp1AxF-FgWk",
            "steps": [
                ("Learn Scikit-learn and model building", "https://www.youtube.com/watch?v=0Lt9w-BxKFQ"),
                ("Apply ML algorithms like Decision Trees, SVM, KNN", "https://www.youtube.com/watch?v=Og847HVwRSI"),
                ("Work with real-world datasets (Titanic, House Prices)", "https://www.kaggle.com/competitions"),
                ("Practice feature engineering techniques", "https://www.youtube.com/watch?v=4so1CxXYiF4"),
                ("Explore evaluation metrics and model tuning", "https://www.youtube.com/watch?v=85dtiMz9tSo")
            ]
        },
        "Advanced": {
            "note": "You should be confident in ML basics, model tuning, and basic data pipelines.",
            "revise": "https://www.youtube.com/watch?v=LHBE6Q9XlzI",
            "steps": [
                ("Study Deep Learning with TensorFlow or PyTorch", "https://www.youtube.com/watch?v=aircAruvnKk"),
                ("Build Neural Networks for classification and regression", "https://www.youtube.com/watch?v=UJwK6jAStmg"),
                ("Work on NLP or Time Series Projects", "https://www.youtube.com/watch?v=0bMe_vCZo30"),
                ("Explore MLOps and model deployment", "https://www.youtube.com/watch?v=K3dLogJebio"),
                ("Contribute to open-source or Kaggle competitions", "https://www.kaggle.com/competitions")
            ]
        }
    },

    "Artificial Intelligence": {
        "Beginner": {
            "note": "Start learning Python and mathematical foundations like linear algebra and probability.",
            "steps": [
                ("Learn Python basics", "https://www.youtube.com/watch?v=rfscVS0vtbw"),
                ("Get started with NumPy and Pandas", "https://www.youtube.com/watch?v=vmEHCJofslg"),
                ("Understand what AI is and its applications", "https://www.youtube.com/watch?v=2ePf9rue1Ao"),
                ("Build small rule-based systems", "https://www.geeksforgeeks.org/expert-systems-in-artificial-intelligence/"),
                ("Explore beginner projects like Tic-Tac-Toe AI", "")
            ]
        },
        "Intermediate": {
            "note": "If you're familiar with Python and ML concepts, start exploring deep learning.",
            "revise": "https://www.youtube.com/watch?v=aircAruvnKk",
            "steps": [
                ("Learn neural networks (basic MLPs)", "https://www.youtube.com/watch?v=8gzWgeUBxYs"),
                ("Implement CNNs for image classification", "https://www.youtube.com/watch?v=YRhxdVk_sIs"),
                ("Understand NLP basics with RNNs or Transformers", "https://www.youtube.com/watch?v=8rXD5-xhemo"),
                ("Do hands-on projects using datasets like MNIST or IMDB", "https://www.kaggle.com/datasets"),
                ("Explore HuggingFace models", "https://huggingface.co/models")
            ]
        },
        "Advanced": {
            "note": "Make sure you're confident in DL architectures, CNNs, RNNs, transformers.",
            "revise": "https://www.youtube.com/watch?v=3ar3-4zIQ6c",
            "steps": [
                ("Fine-tune pretrained models (BERT, GPT)", "https://www.youtube.com/watch?v=8rXD5-xhemo"),
                ("Build custom models using PyTorch/TensorFlow", "https://www.youtube.com/watch?v=EMXfZB8FVUA"),
                ("Experiment with reinforcement learning", "https://www.youtube.com/watch?v=2pWv7GOvuf0"),
                ("Contribute to AI open-source repos", "https://github.com/topics/artificial-intelligence"),
                ("Study AI ethics, interpretability, and fairness", "https://www.youtube.com/watch?v=ioiZatlZtGU")
            ]
        }
    },
   
    "Web Development": {
        "Beginner": {
            "note": "Begin by learning the web fundamentals: HTML, CSS, and JavaScript.",
            "steps": [
                ("Learn HTML5 and CSS3", "https://www.youtube.com/watch?v=UB1O30fR-EE"),
                ("Practice layout with Flexbox and Grid", "https://www.youtube.com/watch?v=fYq5PXgSsbE"),
                ("Understand how websites work (DNS, HTTP, etc.)", "https://www.youtube.com/watch?v=7_LPdttKXPc"),
                ("Build static pages and small projects", ""),
                ("Intro to Git and GitHub", "https://www.youtube.com/watch?v=RGOj5yH7evk")
            ]
        },
        "Intermediate": {
            "note": "Once you're comfortable with the basics, start learning JS frameworks and backend.",
            "revise": "https://www.youtube.com/watch?v=PkZNo7MFNFg",
            "steps": [
                ("Learn JavaScript ES6+ concepts", "https://www.youtube.com/watch?v=hdI2bqOjy3c"),
                ("Build apps using React", "https://www.youtube.com/watch?v=bMknfKXIFA8"),
                ("Explore REST APIs", "https://www.youtube.com/watch?v=-MTSQjw5DrM"),
                ("Learn Node.js + Express backend", "https://www.youtube.com/watch?v=l8WPWK9mS5M"),
                ("Create full-stack MERN projects", "https://www.youtube.com/watch?v=7CqJlxBYj-M")
            ]
        },
        "Advanced": {
            "note": "You should now build production-level applications and explore scalability.",
            "revise": "https://www.youtube.com/watch?v=2Ji-clqUYnA",
            "steps": [
                ("Learn state management (Redux, Context API)", "https://www.youtube.com/watch?v=CVpUuw9XSjY"),
                ("Implement authentication & authorization", "https://www.youtube.com/watch?v=2jqok-WgelI"),
                ("Deploy apps on Vercel, Netlify, or AWS", "https://www.youtube.com/watch?v=nhBVL41-_Cw"),
                ("Integrate CI/CD and testing", "https://www.youtube.com/watch?v=1Y8bYav5XfA"),
                ("Contribute to open-source web projects", "https://github.com/topics/web-development")
            ]
        }
    },

    "Cyber Security": {
        "Beginner": {
            "note": "Understand the fundamentals of cybersecurity and networking.",
            "steps": [
                ("Learn Networking Basics (OSI Model, TCP/IP)", "https://www.youtube.com/watch?v=qiQR5rTSshw"),
                ("Explore Linux for security", "https://www.youtube.com/watch?v=IV4IjHz2yIo"),
                ("Understand Firewalls and VPNs", "https://www.youtube.com/watch?v=3z6z6HY6GOs"),
                ("Practice on TryHackMe or HackTheBox", "https://tryhackme.com/"),
                ("Basic encryption and hashing concepts", "https://www.youtube.com/watch?v=GSIDS_lvRv4")
            ]
        },
        "Intermediate": {
            "note": "Focus on identifying vulnerabilities and ethical hacking techniques.",
            "revise": "https://www.youtube.com/watch?v=GH9aE_h-z3c",
            "steps": [
                ("Study OWASP Top 10", "https://owasp.org/www-project-top-ten/"),
                ("Use Burp Suite and Wireshark", "https://www.youtube.com/watch?v=lf5d-R8LZ2g"),
                ("Learn web app pentesting", "https://www.youtube.com/watch?v=sJd8ayF5d9M"),
                ("Understand cryptographic attacks", "https://www.youtube.com/watch?v=GKNX3tFXABk"),
                ("Explore Capture The Flag (CTF) challenges", "https://www.hackthebox.com/")
            ]
        },
        "Advanced": {
            "note": "Advance your knowledge in malware analysis and threat detection.",
            "revise": "https://www.youtube.com/watch?v=cLvk7uwPZQ8",
            "steps": [
                ("Reverse engineering and malware analysis", "https://www.youtube.com/watch?v=olqzW2PMyoQ"),
                ("Implement intrusion detection systems (IDS)", "https://www.youtube.com/watch?v=iNxi3wE3lsQ"),
                ("Understand red teaming and threat hunting", "https://www.youtube.com/watch?v=j3e4GI9VFCk"),
                ("Study cybersecurity policies and frameworks", "https://www.youtube.com/watch?v=sR1Nnl2OKYQ"),
                ("Contribute to open-source security projects", "https://github.com/topics/cybersecurity")
            ]
        }
    },

    "App Development": {
        "Beginner": {
            "note": "Start learning either native or cross-platform development.",
            "steps": [
                ("Learn Dart & Flutter OR Java/Kotlin for Android", "https://www.youtube.com/watch?v=VPvVD8t02U8"),
                ("Understand app UI components", "https://www.youtube.com/watch?v=x0uinJvhNxI"),
                ("Build your first simple app", "https://www.youtube.com/watch?v=1gDhl4leEzA"),
                ("Use emulator for testing", ""),
                ("Study app lifecycle", "https://developer.android.com/guide/components/activities/activity-lifecycle")
            ]
        },
        "Intermediate": {
            "note": "Deepen your skills in API integration and local storage.",
            "revise": "https://www.youtube.com/watch?v=5gk4U4w8T6o",
            "steps": [
                ("Learn Firebase or SQLite for local storage", "https://www.youtube.com/watch?v=2Vf1D-rUMwE"),
                ("Handle form validations and state", "https://www.youtube.com/watch?v=lkF0TQJO0bA"),
                ("Work on multi-screen navigation", "https://www.youtube.com/watch?v=Z9QbYZh1YXY"),
                ("Integrate REST APIs", "https://www.youtube.com/watch?v=1gDhl4leEzA"),
                ("Create a portfolio-level app", "")
            ]
        },
        "Advanced": {
            "note": "You should now optimize and publish your apps.",
            "revise": "https://www.youtube.com/watch?v=Otl7YNJmAtM",
            "steps": [
                ("Implement advanced state management (Provider/Bloc)", "https://www.youtube.com/watch?v=lxRdgaIRH5E"),
                ("Add push notifications & analytics", "https://www.youtube.com/watch?v=lxRdgaIRH5E"),
                ("Deploy apps to Google Play Store", "https://www.youtube.com/watch?v=KoVx1GcUyF0"),
                ("Handle crash reporting and feedback", "https://www.youtube.com/watch?v=jCbJ-8sK5do"),
                ("Build enterprise-level apps", "")
            ]
        }
    },

    "UI/UX Design": {
        "Beginner": {
            "note": "Learn design principles and prototyping tools like Figma.",
            "steps": [
                ("Study design fundamentals (color, typography)", "https://www.youtube.com/watch?v=_DBBgGsbzRU"),
                ("Learn Figma for wireframing", "https://www.youtube.com/watch?v=4W4LvJnNegg"),
                ("Create your first mockup", ""),
                ("Understand UX writing and flows", "https://www.youtube.com/watch?v=3t9LSjL6Z54"),
                ("Practice with daily UI challenges", "https://www.dailyui.co/")
            ]
        },
        "Intermediate": {
            "note": "Now start working on real-world case studies and interactions.",
            "revise": "https://www.youtube.com/watch?v=_DBBgGsbzRU",
            "steps": [
                ("Prototype using Figma interactions", "https://www.youtube.com/watch?v=S4coA96YqS4"),
                ("Do UI redesigns of popular apps", ""),
                ("Learn about accessibility in design", "https://www.youtube.com/watch?v=4FtyM2JzKcs"),
                ("Document and present your designs", ""),
                ("Update your portfolio with feedback loops", "")
            ]
        },
        "Advanced": {
            "note": "Focus on leadership, research, and team collaboration.",
            "revise": "https://www.youtube.com/watch?v=3v1V2GlEPo8",
            "steps": [
                ("Conduct user interviews and usability testing", "https://www.youtube.com/watch?v=lH3Usi3MQz8"),
                ("Design systems and scalable UI kits", "https://www.youtube.com/watch?v=xv7I3jN1Hp0"),
                ("Collaborate with developers using handoff tools", "https://www.youtube.com/watch?v=rIh_m1LzpAw"),
                ("Run A/B testing and analyze results", "https://www.youtube.com/watch?v=vz8CCf1K6g8"),
                ("Lead a team project end-to-end", "")
            ]
        }
    }
}

# Show Roadmap
if st.button("Generate My Roadmap"):
    data = roadmaps.get(domain, {}).get(track)
    if not data:
        st.warning("Roadmap not available yet for this domain and level.")
    else:
        st.subheader("Your Personalized Roadmap")
        st.markdown(f"**Note:** {data.get('note')}")
        if "revise" in data:
            st.markdown(f"If you're not confident, quickly revise basics: [Watch this video]({data['revise']})")

        st.markdown("### Steps to Follow:")
        for title, link in data["steps"]:
            if link:
                st.markdown(f"- [{title}]({link})")
            else:
                st.markdown(f"- {title}")