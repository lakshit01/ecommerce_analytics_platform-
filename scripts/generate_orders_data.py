from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

# Ensure the data directory exists
os.makedirs("data", exist_ok=True)

# --- 1. DYNAMICALLY LOAD YOUR ACTUAL PRODUCT TABLE ---
# This reads your real products file. Change the path if your file is located elsewhere.
df_products = pd.read_csv("data/products.csv") 

# --- 2. CREATE THE LOOKUP MAP FROM YOUR FILE ---
# This automatically pairs your real 'product_id' and 'price' columns
product_price_map = dict(zip(df_products["product_id"], df_products["unit_price"]))
all_product_ids = list(product_price_map.keys())

# --- 3. GENERATE ORDERS ---
rows = []

for i in range(1, 100001):
    # Pick a random product ID that actually exists in your products.csv
    p_id = random.choice(all_product_ids)
    
    # Pick a random quantity
    qty = random.randint(1, 10)
    
    # Look up the real price from your file and calculate total amount
    unit_price = product_price_map[p_id]
    total_amount = round(unit_price * qty, 2)

    rows.append([
        i,                                      # order_id
        random.randint(1, 5000),                # customer_id (1 to 5000)
        p_id,                                   # product_id
        qty,                                    # quantity
        total_amount,                           # amount
        fake.date_between('-3y', 'today')       # order_date
    ])

df_orders = pd.DataFrame(
    rows,
    columns=[
        "order_id",
        "customer_id",
        "product_id",
        "quantity",
        "amount",
        "order_date"
    ]
)

df_orders.to_csv("data/orders.csv", index=False)
print(f"Successfully generated orders using {len(all_product_ids)} unique products from products.csv!")
