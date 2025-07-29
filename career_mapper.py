from skill_role_mapper import map_skills_to_roles

def map_degree_to_suggestions(degree, skills):
    degree = degree.lower()
    suggestions = []

    if "high school" in degree:
        suggestions.append("You have a great start. Focus on building foundational knowledge through platforms like Coursera, edX, and Khan Academy.")
        suggestions.append("Consider pursuing a diploma or undergraduate degree in your domain of interest.")

    elif "diploma" in degree:
        suggestions.append("Consider transitioning into a full-time Bachelor's program or taking up internships.")
        suggestions.append("Start building real-world projects and deepen your domain expertise.")

    elif "b.tech" in degree or "engineering" in degree:
        suggestions.append("Start preparing for internships or placements. Build a strong project portfolio and contribute to open-source if possible.")

    elif "graduate" in degree:
        suggestions.append("Consider specialization via certifications or a Master's degree.")
        suggestions.append("Start applying your skills in practical work such as freelancing or collaborative projects.")

    elif "postgraduate" in degree:
        suggestions.append("You can now pursue advanced roles in your domain. Consider mentoring juniors, contributing to technical blogs, or building scalable products.")

    else:
        suggestions.append("Keep learning and updating your skillset. There’s no fixed path — just keep building, applying, and growing.")

    return suggestions


def generate_career_advice(name, degree, domain, skills, other_skills=None):
    all_skills = skills + (other_skills or [])
    skill_based_roles, recommended_skills = map_skills_to_roles(all_skills)
    degree_suggestions = map_degree_to_suggestions(degree, skills)

    message = []

    message.append(f"Hello {name},")
    message.append(f"Based on your degree: **{degree}** and preferred domain: **{domain}**")

    if skills:
        message.append(f"You are currently skilled in: **{', '.join(skills)}**")
    if other_skills:
        message.append(f"Other skills you entered: **{', '.join(other_skills)}**")

    message.append("\nSuggested Career Roles for You:")
    message.extend([f"- {role}" for role in skill_based_roles])

    if recommended_skills:
        message.append("\nSkills you may also consider learning:")
        message.extend([f"- {skill}" for skill in recommended_skills])

    message.append("\nAdvice Based on Your Education Level:")
    message.extend([f"- {tip}" for tip in degree_suggestions])

    message.append("\nStay consistent and keep growing in your chosen path.")

    return "\n".join(message)

def generate_track_roadmap(track_level, base_roadmap):
    track_modifiers = {
        "Beginner": lambda step: f"Start with: {step}",
        "Intermediate": lambda step: f"Deepen with: {step}",
        "Advanced": lambda step: f"Master by: {step}"
    }
    modifier = track_modifiers.get(track_level, lambda x: x)
    return [modifier(step) for step in base_roadmap]