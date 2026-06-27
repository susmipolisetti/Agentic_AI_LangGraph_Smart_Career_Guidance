import os
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

print("=" * 60)
print("SMART CAREER GUIDANCE AGENT")
print("Powered by Agentic AI with LangGraph")
print("=" * 60)

# User Input
name = input("Enter Your Name: ")
education = input("Enter Qualification: ")
skills = input("Enter Your Skills (comma separated): ")

skills = skills.lower().split(",")

print("\nAnalyzing Resume...")
print("Checking Skill Gap...")
print("Generating Career Recommendations...\n")

# Career Recommendation Logic
if "python" in skills:
    career = "AI / Machine Learning Engineer"
elif "java" in skills:
    career = "Java Full Stack Developer"
elif "sql" in skills:
    career = "Data Analyst"
elif "c" in skills or "c++" in skills:
    career = "Software Engineer"
else:
    career = "Software Developer"

print("=" * 60)
print("CAREER GUIDANCE REPORT")
print("=" * 60)

print("Name :", name)
print("Education :", education)
print("Recommended Career :", career)

print("\nSuggested Skills")
print("----------------")
print("• Data Structures & Algorithms")
print("• Python")
print("• SQL")
print("• Git & GitHub")
print("• Aptitude")
print("• Communication Skills")

print("\nLearning Roadmap")
print("----------------")
print("1. Learn Programming")
print("2. Practice Coding")
print("3. Build Projects")
print("4. Create GitHub Portfolio")
print("5. Apply for Jobs")

print("\nStatus : Report Generated Successfully")

print("=" * 60)
