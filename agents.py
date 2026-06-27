class ResumeAnalysisAgent:

    def analyze_resume(self, resume_data):
        skills = resume_data.get("skills", [])
        education = resume_data.get("education", "")

        return {
            "skills": skills,
            "education": education
        }


class SkillGapAgent:

    REQUIRED_SKILLS = [
        "Python",
        "SQL",
        "Git",
        "GitHub",
        "Data Structures",
        "Communication"
    ]

    def find_skill_gap(self, skills):
        missing = []

        for skill in self.REQUIRED_SKILLS:
            if skill.lower() not in [s.strip().lower() for s in skills]:
                missing.append(skill)

        return missing


class CareerRecommendationAgent:

    def recommend(self, skills):

        skills = [s.lower() for s in skills]

        if "python" in skills:
            return "AI / Machine Learning Engineer"

        elif "java" in skills:
            return "Java Full Stack Developer"

        elif "sql" in skills:
            return "Data Analyst"

        elif "c++" in skills:
            return "Software Engineer"

        return "Software Developer"


class LearningRoadmapAgent:

    def generate(self):

        return [
            "Learn Python",
            "Practice DSA",
            "Learn SQL",
            "Build Projects",
            "Learn Git & GitHub",
            "Practice Aptitude",
            "Apply for Jobs"
        ]


class JobMatchingAgent:

    def suggest_jobs(self):

        return [
            "Software Engineer",
            "Python Developer",
            "AI Engineer",
            "Data Analyst",
            "ML Engineer"
        ]
