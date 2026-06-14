from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

# Ensure the data directory exists
os.makedirs("data", exist_ok=True)

# --- 1. LOAD YOUR GENERATED ORDERS ---
# We need this to ensure returns match real, existing orders
df_orders = pd.read_csv("data/orders.csv")

# Convert order_date to datetime so we can do date math easily
df_orders["order_date"] = pd.to_datetime(df_orders["order_date"])

# --- 2. SAMPLE 10,000 UNIQUE ORDERS FOR RETURNS ---
# A single order usually gets returned only once, so we sample without replacement
sampled_orders = df_orders.sample(n=10000, random_state=42).to_dict(orient="records")

# --- 3. GENERATE RETURNS DATA ---
return_rows = []

for i, order in enumerate(sampled_orders, start=1):
    order_id = order["order_id"]
    original_amount = order["amount"]
    order_date = order["order_date"]
    
    # Simulate partial vs full returns (return amount can't exceed original amount)
    # Randomly refund anywhere from 50% to 100% of the original purchase amount
    refund_percentage = random.uniform(0.5, 1.0)
    return_amount = round(original_amount * refund_percentage, 2)
    
    # Return date must happen AFTER the order date (e.g., within 1 to 30 days)
    days_to_return = random.randint(1, 30)
    return_date = order_date + pd.Timedelta(days=days_to_return)
    
    # Format date back to standard string YYYY-MM-DD
    return_date_str = return_date.strftime("%Y-%m-%d")
    
    return_rows.append([
        i,                # return_id
        order_id,         # order_id
        return_amount,    # return_amount
        return_date_str   # return_date
    ])

# --- 4. SAVE TO CSV ---
df_returns = pd.DataFrame(
    return_rows,
    columns=["return_id", "order_id", "return_amount", "return_date"]
)

df_returns.to_csv("data/returns.csv", index=False)
print("Successfully generated 10,000 realistic records in data/returns.csv!")
