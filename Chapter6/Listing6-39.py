import pandas as pd
import re

# Sample data with numbers embedded in text
survey = pd.DataFrame({
    "response": ["Height: 5.8 feet", 
                 "Weight: 150 lbs", 
                 "Age: 22 years", 
                 "Income: $45,000", 
                 "Score: 85.5%"]
})

# Extract numbers using regular expressions
survey["number"] = survey["response"].str.extract(r"([\d,]+[\.]?\d*)")
survey["number"] = survey["number"].str.replace(',', '')  # Remove commas
survey["number"] = pd.to_numeric(survey["number"])

print("After extracting numbers:")
print(survey)