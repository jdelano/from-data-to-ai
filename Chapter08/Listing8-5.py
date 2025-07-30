import pandas as pd

emp = pd.DataFrame({
    "emp_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Cathy", "Dan"],
    "dept_id": [10, 20, 30, 40] 
})
dept = pd.DataFrame({
    "dept_id": [10, 20, 30, 50],
    "dept_name": ["Sales", "Engineering", 
                  "HR", "Marketing"]
})

# Demonstrate different join types
print("=== INNER JOIN ===")
inner_result = pd.merge(emp, dept, on="dept_id", how="inner")
print(inner_result)

print("=== LEFT JOIN ===")
left_result = pd.merge(emp, dept, on="dept_id", how="left")
print(left_result)

print("=== RIGHT JOIN ===")
right_result = pd.merge(emp, dept, on="dept_id", how="right")
print(right_result)

print("=== FULL OUTER JOIN ===")
outer_result = pd.merge(emp, dept, on="dept_id", how="outer")
print(outer_result)