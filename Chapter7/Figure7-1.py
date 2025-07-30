import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set random seed for reproducibility
np.random.seed(42)

# Generate symmetric data (test scores)
test_scores = np.random.normal(75, 10, 1000)
test_scores = np.clip(test_scores, 0, 100)  # Keep scores between 0-100

# Generate skewed data (household income)
# Most people earn 30k-80k
normal_incomes = np.random.normal(55000, 15000, 100)
normal_incomes = np.clip(normal_incomes, 20000, 100000)

# A few high earners
high_incomes = np.random.uniform(200000, 1000000, 40)

# One billionaire
billionaire = [1500000]

# Combine all incomes
household_income = np.concatenate([normal_incomes, high_incomes, billionaire])
book_blue = "#8CB3E6"
book_gold = "#FA8500"
book_green = "#339900"
plt.rcParams["font.family"] = "Myriad Pro"
# Create the plot with high DPI
plt.figure(figsize=(12, 5), dpi=300)

# Symmetric distribution (test scores)
plt.subplot(1, 2, 1)
plt.hist(test_scores, bins=30, color=book_blue, edgecolor="black", alpha=0.7, linewidth=0.5)
plt.title("Symmetric Distribution\n(Test Scores)", fontsize=14, pad=10)
plt.xlabel("Score", fontsize=12)
plt.ylabel("Number of Students", fontsize=12)
plt.axvline(np.mean(test_scores), color=book_gold, linestyle="-", linewidth=1, label=f"Mean: {np.mean(test_scores):.1f}")
plt.axvline(np.median(test_scores), color=book_green, linestyle="--", linewidth=1, label=f"Median: {np.median(test_scores):.1f}")
plt.legend(loc="upper left", fontsize=12)
plt.grid(True, alpha=0.3)

# Skewed distribution (income)
plt.subplot(1, 2, 2)
plt.hist(household_income, bins=50, color=book_blue, edgecolor="black", alpha=0.7, linewidth=0.5)
plt.title("Skewed Distribution\n(Household Income)", fontsize=14, pad=10)
plt.xlabel("Income ($)", fontsize=12)
plt.ylabel("Number of Households", fontsize=12)
plt.axvline(np.mean(household_income), color=book_gold, linestyle="-", linewidth=1, label=f"Mean: ${np.mean(household_income):,.0f}")
plt.axvline(np.median(household_income), color=book_green, linestyle="--", linewidth=1, label=f"Median: ${np.median(household_income):,.0f}")
plt.legend(loc="upper right", fontsize=12)
plt.grid(True, alpha=0.3)

# Format x-axis for income to show values in thousands
ax = plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x/1000:.0f}k"))

# Add curly brace annotation
y_position = 70  # Height where the brace will be placed
mean_income = np.mean(household_income)
median_income = np.median(household_income)


# Simple horizontal line with brackets approach (easier)
bracket_height = 75
# Left bracket
plt.plot([median_income, median_income], [bracket_height - 1, bracket_height + 1], "k-", linewidth=1.5)
# Right bracket  
plt.plot([mean_income, mean_income], [bracket_height - 1, bracket_height + 1], "k-", linewidth=1.5)
# Horizontal line
plt.plot([median_income, mean_income], [bracket_height, bracket_height], "k-", linewidth=1.5)

# Add text above the bracket
# Calculate middle of bracket
bracket_middle = (median_income + mean_income) / 2

# Add text with arrow
text_x = mean_income + 5000
text_y = bracket_height - 15

#plt.text(mean_income + 5000, bracket_height - 10, 
 #       f"Difference: ${(mean_income - median_income):,.0f}", 
  #       ha="left", fontsize=10, fontweight="bold")

plt.annotate(f"Difference: ${(mean_income - median_income):,.0f}",
             xy=(bracket_middle, bracket_height),  # Point arrow TO
             xytext=(text_x, text_y),  # Point arrow FROM (text location)
             ha="left", 
             fontsize=12, 
             arrowprops=dict(arrowstyle="->", 
                           connectionstyle="arc3,rad=0",
                           color="black",
                           lw=1))

# Add annotation for the outlier that's to the right
plt.annotate("One household\nearns $1.5M", xy=(1_500_000, 1), xytext=(1_500_000, 10), fontsize=12, ha="right", arrowprops=dict(arrowstyle="->", 
                           connectionstyle="arc3,rad=0",
                           color="black",
                           lw=1))

plt.tight_layout()
plt.savefig("Chapter7/07-Figure7-1.png", dpi=300, bbox_inches="tight")
plt.show()