import streamlit as st

st.set_page_config(page_title="Smart Career Guidance Agent")

st.title("🚀 Smart Career Guidance Agent")

name = st.text_input("Enter Your Name")
education = st.text_input("Qualification")
skills = st.text_area("Enter Skills (comma separated)")

if st.button("Analyze Resume"):

    skills_list = [s.strip().lower() for s in skills.split(",")]

    if "python" in skills_list:
        career = "AI / Machine Learning Engineer"
    elif "java" in skills_list:
        career = "Java Full Stack Developer"
    elif "sql" in skills_list:
        career = "Data Analyst"
    else:
        career = "Software Developer"

    st.success("Analysis Completed")

    st.subheader("Career Recommendation")
    st.write(career)

    st.subheader("Learning Roadmap")

    st.write("• Learn Python")
    st.write("• Practice DSA")
    st.write("• Learn SQL")
    st.write("• Build Projects")
    st.write("• Apply for Jobs")
