import pandas as pd
import matplotlib.pyplot as plt

# Sample student data with obvious problems
student_data = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "study": [15, 20, 12, 18, -5, 25, 16, 14, 22, 19]
})

# Create box plot to visualize outliers
student_data.plot(kind="box", column="study")
plt.title("Study Hours Distribution")
plt.show()