import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate skewed call center data with more realistic distribution
# Most calls 5-20 minutes
normal_calls = np.random.normal(12, 5, 700)
normal_calls = np.clip(normal_calls, 3, 25)

# Some longer calls 25-60 minutes
moderate_calls = np.random.uniform(25, 60, 250)

# A few very long calls
long_calls = np.random.uniform(60, 180, 50)

# Combine all calls
response_times = np.concatenate([normal_calls, moderate_calls, long_calls])

# Apply reciprocal transform (calls per minute)
response_speeds = 1 / response_times

# Your book colors
book_blue = "#8CB3E6"
book_gold = "#FA8500"
book_green = "#339900"

# Create the plot
plt.figure(figsize=(12, 5), dpi=300)
plt.rcParams["font.family"] = "Myriad Pro"

# Original skewed data
plt.subplot(1, 2, 1)
plt.hist(response_times, bins=40, color=book_blue, edgecolor="black", alpha=0.7, linewidth=0.5)
plt.title("Original Data: Response Times\n(Right-Skewed)", fontsize=14, pad=10)
plt.xlabel("Minutes per Call", fontsize=12)
plt.ylabel("Number of Calls", fontsize=12)
plt.xlim(0, 200)
mean1 = np.mean(response_times)
median1 = np.median(response_times)
plt.axvline(mean1, color=book_gold, linestyle="-", linewidth=1, 
            label=f"Mean: {mean1:.1f} min")
plt.axvline(median1, color=book_green, linestyle="--", linewidth=1, 
            label=f"Median: {median1:.1f} min")
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Reciprocal transformed data  
plt.subplot(1, 2, 2)
plt.hist(response_speeds, bins=40, color=book_blue, edgecolor="black", alpha=0.7, linewidth=0.5)
plt.title("After Reciprocal Transform: Call Speed\n(Less Skewed)", fontsize=14, pad=10)
plt.xlabel("Calls per Minute", fontsize=12)
plt.ylabel("Number of Calls", fontsize=12)
plt.xlim(0, 0.35)
mean2 = np.mean(response_speeds)
median2 = np.median(response_speeds)
plt.axvline(mean2, color=book_gold, linestyle="-", linewidth=1, 
            label=f"Mean: {mean2:.3f}")
plt.axvline(median2, color=book_green, linestyle="--", linewidth=1, 
            label=f"Median: {median2:.3f}")
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("Chapter7/07-Figure7-2.png", dpi=300, bbox_inches="tight")
plt.show()