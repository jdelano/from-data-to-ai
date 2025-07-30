import pandas as pd

sizes = pd.DataFrame({
    "product": ["Shirt", "Jacket", "Pants", "Hat",
                "Dress"],
    "size": ["S", "M", "L", "M", "S"]
})

size_order = {
    "S": 1, 
    "M": 2, 
    "L": 3
}
sizes["size_numeric"] = sizes["size"].apply(
    lambda size: size_order[size]
)
print(sizes)
average_size = sizes["size_numeric"].mean()
print(f"Average size: {average_size}")