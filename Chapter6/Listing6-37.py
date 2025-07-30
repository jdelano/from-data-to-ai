import pandas as pd

# Data with synonyms and abbreviations
courses = pd.DataFrame({
    "student": ["Al", "Bob", "Chuck", "Dan"],
    "major": ["CS", "Computer Science", "Bio", "Biology"],
    "status": ["FT", "Full Time", "PT", "Part Time"]
})

# Create mapping dictionaries to standardize variations
major_mapping = {
    "cs": "Computer Science",
    "computer science": "Computer Science",
    "bio": "Biology",
    "biology": "Biology"
}

status_mapping = {
    "ft": "Full Time",
    "full time": "Full Time",
    "pt": "Part Time", 
    "part time": "Part Time",
}

# Normalize case, apply mappings, and format final output
courses["major"] = (courses["major"]
                        .str.lower()
                        .replace(major_mapping)
                        .str.title())

courses["status"] = (courses["status"]
                        .str.lower()
                        .replace(status_mapping)
                        .str.title())

print("After standardizing variations:")
print(courses)
