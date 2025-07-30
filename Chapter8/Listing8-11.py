import pandas as pd

warehouse_a = pd.DataFrame({
    "product_id": ["P001", "P002", "P003"],
    "product_name": ["Widget", "Gadget", "Doohickey"],
    "weight_kg": [2.5, 1.2, 3.8] # Warehouse A uses kilograms
})


warehouse_b = pd.DataFrame({
    "product_id": ["P002", "P003", "P004"],
    "location": ["Aisle 3", "Aisle 1", "Aisle 5"],
    "weight_lbs": [2.65, 8.38, 4.41] # Warehouse B uses pounds
})

# Convert pounds to kilograms (1 lb = 0.453592 kg)
warehouse_b["weight_kg"] = warehouse_b["weight_lbs"] * 0.453592

# Now merge on product_id
merged = pd.merge(warehouse_a, warehouse_b, on="product_id", how="outer")
print("=== After unit conversion ===")
print(merged)

# Check if weights match (allowing for rounding)
merged["weight_match"] = abs(merged["weight_kg_x"] - merged["weight_kg_y"]) < 0.01
print("=== Weight verification ===")
print(merged[["product_id", "weight_kg_x", "weight_kg_y", "weight_match"]])
