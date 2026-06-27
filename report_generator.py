def generate_report(result):

    print("\n========== CAREER GUIDANCE REPORT ==========")

    print("Recommended Career:")
    print(result["career"])

    print("\nMissing Skills:")
    for skill in result["missing_skills"]:
        print("-", skill)

    print("\nLearning Roadmap:")
    for step in result["roadmap"]:
        print("-", step)

    print("\nSuggested Jobs:")
    for job in result["jobs"]:
        print("-", job)

    print("\n========== END OF REPORT ==========")
