import pandas as pd

q1q2 = pd.DataFrame({
    'Quarter': ['Q1', 'Q2'],
    'Revenue': [1000, 1500]
})

q3q4 = pd.DataFrame({
    'Quarter': ['Q3', 'Q4'],
    'Revenue': [2000, 2500]
})

# Add source labels to each data frame
q1q2['Source'] = 'Q1-Q2_Report'
q3q4['Source'] = 'Q3-Q4_Report'

# Stack the data frames
year_data = pd.concat([q1q2, q3q4], ignore_index=True)
print(year_data)
