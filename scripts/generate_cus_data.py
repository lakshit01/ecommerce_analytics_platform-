from faker import Faker
import pandas as pd
import random

fake = Faker()

rows = []

for i in range(1,5001):

    rows.append([
        i,
        fake.first_name(),
        fake.last_name(),
        fake.email(),
        fake.city(),
        fake.state(),
        fake.date_between('-3y','today')
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "customer_id",
        "first_name",
        "last_name",
        "email",
        "city",
        "state",
        "signup_date"
    ]
)

df.to_csv("data/customers.csv", index=False)