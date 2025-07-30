import pandas as pd
import matplotlib.pyplot as plt

# Sample study performance data
study_data = {
    "HoursStudied": [2, 4, 6, 8, 10, 3, 5, 7, 9, 
                     1, 10, 6, 8, 4, 2],
    "ExamScore": [65, 70, 78, 85, 92, 68, 75, 
                  82, 88, 60, 30, 80, 87, 72, 63]
}

df = pd.DataFrame(study_data)

# Set figure size and DPI for high resolution
plt.figure(figsize=(8, 6), dpi=300)

# Create the scatterplot using Pandas
df.plot(kind="scatter", 
        x="HoursStudied", 
        y="ExamScore", 
        alpha=0.7
)

# Customize with Matplotlib
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score (%)")
plt.title("Study Time vs. Exam Performance")
plt.grid(True, alpha=0.3)
plt.ylim(0, None)
plt.savefig("Chapter5/05-Figure5-3.png", dpi=300, bbox_inches="tight")
plt.show()