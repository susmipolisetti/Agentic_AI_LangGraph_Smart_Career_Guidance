def get_job_recommendations(career):

    jobs = {
        "AI / Machine Learning Engineer": [
            "Machine Learning Engineer",
            "AI Engineer",
            "Python Developer"
        ],
        "Data Analyst": [
            "Data Analyst",
            "Business Analyst"
        ],
        "Software Engineer": [
            "Software Engineer",
            "Backend Developer"
        ]
    }

    return jobs.get(career, ["Software Developer"])
