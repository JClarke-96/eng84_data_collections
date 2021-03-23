# Create a dictionary
devops_student = {
    "key": "value",
    "name": "Jordan",
    "stream": "DevOps",
    "completed_lesson": 3,
    "completed_lesson_names": ["variables", "data types", "collections"]
}

# Add operations to lesson names, increase lessons complete to 4, remove index 1 lesson name
devops_student["completed_lesson_names"].append("operators")
devops_student["completed_lesson"] = 4
devops_student["completed_lesson_names"].remove("data types")

print(devops_student)
print(type(devops_student))
print(devops_student["name"])