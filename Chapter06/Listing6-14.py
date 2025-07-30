import pandas as pd
# Sample data 
test_data = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "Diana"],
    "Score": [85, 150, 78, 95]
})

# Reset scores above 100 to equal 100
test_data["Capped"] = test_data["Score"].apply(
    lambda score: 100 if score > 100 else score
)

print("Test Data:")
print(test_data)

