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

# Convert to DataFrame
df = pd.DataFrame(majors_data)

# Set figure size and DPI for high resolution (wider for two charts)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), dpi=300)

# Left chart - y-axis starts at 0 (honest representation)
df.plot(kind="bar", x="Major", y="StudentCount", legend=False, ax=ax1, color=book_blue)
ax1.set_xlabel("Academic Major")
ax1.set_ylabel("Number of Students")
ax1.set_title("Honest Representation (Y-axis starts at 0)")
ax1.set_ylim(0, None)  # Explicitly start at 0

# Right chart - y-axis starts at 30 (misleading representation)
df.plot(kind="bar", x="Major", y="StudentCount", legend=False, ax=ax2, color=book_blue)
ax2.set_xlabel("Academic Major")
ax2.set_ylabel("Number of Students")
ax2.set_title("Misleading Representation (Y-axis starts at 35)")
ax2.set_ylim(35, None)  # Start at 30 to exaggerate differences

plt.tight_layout()

# Save as high-resolution image
plt.savefig("Chapter5/05-Figure5-5.png", dpi=300, bbox_inches="tight")
plt.show()