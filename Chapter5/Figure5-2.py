import pandas as pd
import matplotlib.pyplot as plt

# Create sample data 
majors_data = {
    "Major": ["Business", "Computer Science", 
              "Cybersecurity", "Psychology", "Other"],
    "StudentCount": [120, 95, 75, 85, 40]
}

df = pd.DataFrame(majors_data)

# Set figure size and DPI for high resolution
plt.figure(figsize=(8, 6), dpi=300)

# Create the pie chart
df.plot(kind="pie", 
        y="StudentCount", 
        labels=df["Major"], 
        autopct='%1.1f%%',
        startangle=90,
        legend=False)
plt.title("Majors Distribution")
plt.axis("equal")  # Ensures the pie chart is circular
plt.savefig("Chapter5/05-Figure5-2.png", dpi=300, bbox_inches="tight")
plt.show()