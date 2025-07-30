import pandas as pd
import matplotlib.pyplot as plt

# Create sample data 
majors_data = {
    "Major": ["Business", "Computer Science", 
              "Cybersecurity", "Psychology", "Other"],
    "StudentCount": [120, 95, 75, 85, 40]
}

# Convert to Data frame
df = pd.DataFrame(majors_data)

# Create the basic chart using Pandas
df.plot(kind="bar", 
        x="Major", 
        y="StudentCount", 
        legend=False
)

# Customize and show using Matplotlib
plt.xlabel("Academic Major")
plt.ylabel("Number of Students")
plt.title("Student Enrollment by Major")
plt.tight_layout()
plt.show()