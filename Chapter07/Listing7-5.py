import pandas as pd

products = pd.DataFrame({
    "product": ["Shirt", "Jacket", "Pants", "Hat"],
    "size": ["S", "M", "L", "M"]
})

products_encoded = pd.get_dummies(products, columns=["size"])
print(products_encoded)
