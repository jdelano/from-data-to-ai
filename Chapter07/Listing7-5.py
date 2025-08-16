import pandas as pd

products = pd.DataFrame({
    "product": ["Shirt", "Jacket", "Pants", "Hat"],
    "color": ["red", "blue", "green", "blue"]
})

products_encoded = pd.get_dummies(products, columns=["color"])
print(products_encoded)