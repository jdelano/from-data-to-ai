import pandas as pd
import numpy as np
import time

def make_data(n_customers=500_000,
              n_products=200_000,
              n_promos=500,
              n_sales=1_000_000):
    # Customers: id, some value
    customers = pd.DataFrame({
        "customer_id": np.arange(n_customers),
        "customer_val": np.random.randn(n_customers)
    })

    # Products: id, category
    products = pd.DataFrame({
        "product_id": np.arange(n_products),
        "category": np.random.choice([f"cat{i}" for i in range(20)], size=n_products)
    })

    # Promotions: map customers → products
    promotions = pd.DataFrame({
        "promo_id": np.arange(n_promos),
        "customer_id": np.random.choice(customers["customer_id"], size=n_promos),
        "product_id":  np.random.choice(products["product_id"],  size=n_promos)
    })

    # Sales (for the later aggregation test)
    sales = pd.DataFrame({
        "sale_id":     np.arange(n_sales),
        "customer_id": np.random.choice(customers["customer_id"], size=n_sales),
        "product_id":  np.random.choice(products["product_id"],  size=n_sales),
        "amount":      np.random.rand(n_sales) * 100
    })

    return customers, products, promotions, sales

def time_join_sequence(seq_name, sequence):
    result = sequence[0][0]
    print(f"\n-- {seq_name} --")
    for i, (df, on, how) in enumerate(sequence[1:], start=2):
        t0 = time.time()
        result = result.merge(df, on=on, how=how)
        t1 = time.time()
        print(f"Step {i}: merge on {on!r}, how={how!r} -> shape {result.shape} (took {t1-t0:.3f}s)")
    return result

if __name__ == "__main__":
    # 1) Create the data
    customers, products, promotions, sales = make_data()

    # 2) Now this will run without KeyError
    seq1 = [
        (customers,  "customer_id", "inner"),
        (promotions, "customer_id", "inner"),
        (products,   "product_id",  "inner"),
        (sales,      "customer_id",  "inner"),
    ]
    res1 = time_join_sequence("Cust→Promo→Prod", seq1)

    # (You can omit or revise seq2 if you don’t actually need that ordering.)
    print("\nFinal shape (Cust→Promo→Prod):", res1.shape)
    seq2 = [
        (customers,  "customer_id", "inner"),
        (sales,      "customer_id", "inner"),
        (products,   "product_id",  "inner"),
        (promotions, "customer_id", "inner"),
    ]
    res2 = time_join_sequence("Cust→Promo→Prod", seq2)
    print("\nFinal shape (Cust→Promo→Prod):", res2.shape)
