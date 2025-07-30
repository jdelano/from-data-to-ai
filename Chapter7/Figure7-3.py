import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate slightly left-skewed participation data
# Core group of good students (6-8.5)
main_group = np.random.normal(7.2, 1.0, 800)
main_group = np.clip(main_group, 4, 9.2)

# Some very good students (8.5-9.8)
very_good = np.random.uniform(8.5, 9.8, 100)

# A few perfect scores
perfect = np.ones(20) * 10

# Some struggling students (0-4)
struggling = np.random.exponential(1.5, 80)
struggling = np.clip(struggling, 0, 4)

# Combine all scores
participation_scores = np.concatenate([main_group, very_good, perfect, struggling])

# Apply square transform
squared_scores = participation_scores ** 2

# Your book colors
book_blue = "#8CB3E6"
book_gold = "#FA8500"
book_green = "#339900"

# Create the plot
plt.figure(figsize=(12, 5), dpi=300)
plt.rcParams["font.family"] = "Myriad Pro"

# Original left-skewed data
plt.subplot(1, 2, 1)
plt.hist(participation_scores, bins=30, color=book_blue, edgecolor="black", alpha=0.7, linewidth=0.5)
plt.title("Original Data: Participation Scores\n(Left-Skewed)", fontsize=14, pad=10)
plt.xlabel("Score (0-10 scale)", fontsize=12)
plt.ylabel("Number of Students", fontsize=12)
plt.xlim(-0.5, 10.5)
mean1 = np.mean(participation_scores)
median1 = np.median(participation_scores)
plt.axvline(mean1, color=book_gold, linestyle="-", linewidth=1, 
           label=f"Mean: {mean1:.1f}")
plt.axvline(median1, color=book_green, linestyle="--", linewidth=1, 
           label=f"Median: {median1:.1f}")
plt.legend(fontsize=12, loc="upper left")
plt.grid(True, alpha=0.3)

# Square transformed data
plt.subplot(1, 2, 2)
plt.hist(squared_scores, bins=30, color=book_blue, edgecolor="black", alpha=0.7, linewidth=0.5)
plt.title("After Square Transform\n(More Symmetric)", fontsize=14, pad=10)
plt.xlabel("Squared Score", fontsize=12)
plt.ylabel("Number of Students", fontsize=12)
plt.xlim(-5, 105)
mean2 = np.mean(squared_scores)
median2 = np.median(squared_scores)
plt.axvline(mean2, color=book_gold, linestyle="-", linewidth=1, 
           label=f"Mean: {mean2:.1f}")
plt.axvline(median2, color=book_green, linestyle="--", linewidth=1, 
           label=f"Median: {median2:.1f}")
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("Chapter7/07-Figure7-3.png", dpi=300, bbox_inches="tight")
plt.show()