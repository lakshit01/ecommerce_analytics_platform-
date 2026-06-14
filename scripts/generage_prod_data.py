import os
import random
import pandas as pd
from faker import Faker

fake = Faker()

# Define realistic real-world categories and their matching product items
category_mapping = {
    "Electronics": ["Laptop", "Headphones", "Watch", "Smartphone", "Speaker", "Camera"],
    "Apparel & Clothing": ["T-Shirt", "Backpack", "Shoes", "Jacket", "Jeans", "Socks"],
    "Home & Furniture": ["Chair", "Desk", "Sofa", "Dining Table", "Lamp", "Bookshelf"],
    "Fitness & Outdoors": ["Yoga Mat", "Water Bottle", "Dumbbells", "Bicycle", "Tent"]
}

rows = []

# High-quality e-commerce adjectives for building product names
adjectives = ["Wireless", "Ergonomic", "Premium", "Minimalist", "Eco-Friendly", "Smart", "Portable", "Durable"]

for i in range(1, 501):
    # 1. Pick a clean, realistic retail category
    category_name = random.choice(list(category_mapping.keys()))
    
    # 2. Pick an item noun that actually belongs in that category
    product_noun = random.choice(category_mapping[category_name])
    
    # 3. Build a natural product name (e.g., "Smart Wireless Laptop")
    adj1 = random.choice(adjectives)
    adj2 = fake.word().capitalize()  # Generates a random descriptive word
    product_name = f"{adj1} {adj2} {product_noun}"

    rows.append([
        i,
        product_name,
        category_name,
        round(random.uniform(9.99, 1299.99), 2)  # Normal retail price range
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "product_id",
        "product_name",
        "category",
        "unit_price"
    ]
)

# Ensure the output directory exists
os.makedirs("data", exist_ok=True)
df.to_csv("data/products.csv", index=False)

print("Successfully generated clean retail data in 'data/products.csv'!")
