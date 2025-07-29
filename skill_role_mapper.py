skill_role_map = {
    "Python": ["Backend Developer", "Data Analyst", "ML Engineer"],
    "Java": ["Backend Developer", "Android Developer"],
    "C++": ["Software Developer", "Game Developer"],
    "JavaScript": ["Frontend Developer", "Full Stack Developer"],
    "HTML": ["Frontend Developer", "UI/UX Engineer"],
    "CSS": ["Frontend Developer", "UI Designer"],
    "React": ["Frontend Developer", "Full Stack Developer"],
    "Node.js": ["Backend Developer", "Full Stack Developer"],
    "SQL": ["Database Administrator", "Data Analyst"],
    "MongoDB": ["Backend Developer", "Full Stack Developer"],
    "TensorFlow": ["ML Engineer", "AI Researcher"],
    "Pandas": ["Data Analyst", "ML Engineer"],
    "Docker": ["DevOps Engineer", "SRE"],
    "Kubernetes": ["DevOps Engineer", "Cloud Engineer"],
    "Linux": ["System Administrator", "DevOps Engineer"],
    "AWS": ["Cloud Engineer", "DevOps Engineer"],
    "Photoshop": ["UI/UX Designer", "Graphic Designer"],
    "Figma": ["UI/UX Designer", "Product Designer"]
}

def map_skills_to_roles(user_skills):
    user_skills_lower = set(s.lower() for s in user_skills)

    suggested_roles = set()
    recommended_skills = set()

    for skill, roles in skill_role_map.items():
        if skill.lower() in user_skills_lower:
            suggested_roles.update(roles)

    for skill, roles in skill_role_map.items():
        if any(role in suggested_roles for role in roles) and skill.lower() not in user_skills_lower:
            recommended_skills.add(skill)

    return sorted(suggested_roles), sorted(recommended_skills)