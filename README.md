# TechPath Mentor

**TechPath Mentor** is an AI-powered learning and career guidance platform built with **Streamlit**.  
It offers a personalized experience for students and professionals to explore suitable career paths, structured roadmaps, resume building help, certification guidance, and project ideas — all based on their domain and skill level.

---

## Features

### 1. Home
- Welcome screen with overview of platform
- Clean layout and instructions

### 2. Career Suggestions
- Based on skills, education, and interests
- Suggests relevant job roles and domains
- Uses logic-based skill-role mapping

### 3. Roadmap Builder
- Choose domain: Data Science, Web Development, AI, Cyber Security, etc.
- Choose level: Beginner, Intermediate, Advanced
- Returns curated learning roadmap with YouTube links and optional revision videos

### 4. Resume Help
- Tips for writing effective resumes
- Format guidelines and common mistakes to avoid

### 5. Certification Guides
- Top certification suggestions by domain and level
- Trusted platforms: Coursera, edX, Google, etc.

### 6. Project Ideas
- Domain-specific project ideas
- Links to GitHub for reference

### 7. Resume Builder
- Interactive form to input personal and academic details
- Generates a well-formatted PDF resume

---

## Folder Structure

```
TechPath-Mentor/
├── Home.py
├── 1_Career_Suggestions.py
├── 2_Roadmap_Builder.py
├── 3_Resume_Help.py
├── 4_Certification_Guides.py
├── 5_Project Ideas.py
├── 6_Resume_Builder.py
├── career_mapper.py
├── skill_role_mapper.py
├── requirements.txt
└── README.md
```

---

## How to Run the App

### Step 1: Clone this repository
```bash
git clone https://github.com/your-username/TechPath-Mentor.git
cd TechPath-Mentor
```

### Step 2: Create a virtual environment
```bash
python -m venv venv
```

### Step 3: Activate it

- On **Windows**:
```bash
venv\Scripts\activate
```

- On **macOS/Linux**:
```bash
source venv/bin/activate
```

### Step 4: Install the required packages
```bash
pip install -r requirements.txt
```

### Step 5: Run the application
```bash
streamlit run Home.py
```

Then open the link shown in terminal in your browser.

---

## Tech Stack

- Python
- Streamlit
- GitHub
- HTML/CSS (for custom UI)
- YouTube/Kaggle links for content

---

## Acknowledgments
- This project was built as part of the **Elevate Labs Internship**.

---

## Author

**Nikshitha Naradasu**  

---

## License

This project is intended for academic and educational purposes only.  
All third-party links and content belong to their respective owners.
