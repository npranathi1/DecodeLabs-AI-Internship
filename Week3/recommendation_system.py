print("Simple Course Recommendation System")
print("-----------------------------------")

courses = {
    "Python Basics": ["python", "coding", "beginner"],
    "Machine Learning": ["python", "ai", "data", "ml"],
    "Web Development": ["html", "css", "javascript", "web"],
    "Data Analytics": ["data", "excel", "python", "charts"],
    "Cyber Security": ["security", "network", "hacking"],
    "App Development": ["android", "mobile", "app", "java"]
}

print("Available interests:")
print("python, coding, ai, data, ml, web, security, mobile, java, excel")
print()

user_input = input("Enter your interests separated by commas: ")

user_interests = user_input.lower().split(",")

clean_interests = []

for interest in user_interests:
    clean_interests.append(interest.strip())

recommendations = []

for course, tags in courses.items():
    score = 0

    for interest in clean_interests:
        if interest in tags:
            score += 1

    if score > 0:
        recommendations.append((course, score))

recommendations.sort(key=lambda x: x[1], reverse=True)

print()
print("Recommended courses for you:")

if len(recommendations) == 0:
    print("No matching course found. Try using different interests.")
else:
    for course, score in recommendations:
        print(f"{course} - Match Score: {score}")