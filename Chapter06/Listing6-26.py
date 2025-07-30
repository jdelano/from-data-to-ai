import pandas as pd
import matplotlib.pyplot as plt

# Sample student data with obvious problems
student_data = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "study": [15, 20, 12, 18, -5, 25, 16, 14, 22, 19]
})

# Create figure with high DPI
fig, ax = plt.subplots(dpi=300)

# Create box plot to visualize outliers (exactly as original)
student_data.boxplot(column="study", ax=ax)
plt.title("Study Hours Distribution")

# Add annotation for the outlier
ax.annotate('Outlier', 
            xy=(1, -5), 
            xytext=(1.15, -2),
            arrowprops=dict(arrowstyle='->'),
            fontsize=10)

# Save high-DPI version before showing
plt.savefig("Chapter6/06-BoxPlot.png", dpi=300, bbox_inches="tight")

plt.show()