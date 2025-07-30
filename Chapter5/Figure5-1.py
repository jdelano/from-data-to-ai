import pandas as pd
import matplotlib.pyplot as plt

# Create sample data 
majors_data = {
    "Major": ["Business", "Computer Science", "Cybersecurity", "Psychology", "Other"],
    "StudentCount": [120, 95, 75, 85, 40]
}
book_blue = "#8CB3E6"
book_gold = "#FA8500"
book_green = "#339900"

# Set figure size and DPI for high resolution
plt.figure(figsize=(8, 6), dpi=300)

# Convert to Data frame
df = pd.DataFrame(majors_data)

# Create the basic chart using Pandas
df.plot(kind="bar", x="Major", y="StudentCount", legend=False, color=book_blue)

# Customize and show using Matplotlib
plt.xlabel("Academic Major")
plt.ylabel("Number of Students")
plt.title("Student Enrollment by Major")
plt.tight_layout()      

# Save as high-resolution image
plt.savefig("Chapter5/05-Figure5-1.png", dpi=300, bbox_inches="tight")
plt.show()