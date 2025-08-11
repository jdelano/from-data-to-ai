import pandas as pd
import matplotlib.pyplot as plt

# Create sample data 
majors_data = {
    "Major": ["Business", "Computer Science", 
              "Cybersecurity", "Psychology", 
              "Other"],
    "StudentCount": [120, 95, 75, 85, 40]
}
df = pd.DataFrame(majors_data)

# Create the pie chart
df.plot(kind="pie", 
        y="StudentCount", 
        labels=df["Major"], 
        autopct='%1.1f%%',
        startangle=90,
        legend=False)
plt.title("Majors Distribution")
plt.axis("equal")  # Ensures the pie chart is circular
plt.show()