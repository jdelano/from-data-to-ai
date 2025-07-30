import pandas as pd
# Enrollment data (wide format)
enrollment = pd.DataFrame({
    "student_id": [101, 102, 103],
    "fall_2023": ["CS101", "MATH201", "CS101"],
    "spring_2024": ["CS102", "MATH202", "BIO101"]
})

# Course catalog (long format)
catalog = pd.DataFrame({
    "semester": ["fall_2023", "fall_2023", "spring_2024", "spring_2024"],
    "course_id": ["CS101", "MATH201", "CS102", "MATH202"],
    "instructor": ["Dr. Smith", "Dr. Jones", "Dr. Smith", "Dr. Lee"],
    "credits": [3, 4, 3, 4]
})

# Reshape enrollment to long format
enrollment_long = enrollment.melt(
    id_vars="student_id",
    var_name="semester",
    value_name="course_id"
)

# Now we can merge!
merged = pd.merge(enrollment_long, catalog, 
                  on=["semester", "course_id"], 
                  how="left")

print("Integrated enrollment data with course details:")
print(merged)