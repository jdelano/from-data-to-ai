import pandas as pd
import matplotlib.pyplot as plt

# Monthly sales data
sales_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May",
              "Jun", "Jul", "Aug", "Sep", "Oct",
              "Nov", "Dec"],
    "Sales": [45000, 52000, 48000, 61000, 58000,
              67000, 72000, 69000, 63000, 59000,
              54000, 49000]
}

df = pd.DataFrame(sales_data)

# Set figure size and DPI for high resolution
plt.figure(figsize=(8, 6), dpi=300)

# Create the line chart
df.plot(kind="line", 
        x="Month", 
        y="Sales", 
        legend=False, 
        marker="o"
)

# Customize for clarity
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.title("Monthly Sales Performance")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.ylim(0, None)
plt.savefig("Chapter5/05-Figure5-4.png", dpi=300, bbox_inches="tight")
plt.show()
