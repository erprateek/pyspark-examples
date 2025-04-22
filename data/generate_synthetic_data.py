from faker import Faker
import pandas as pd
import random

faker = Faker()

# Generate synthetic transaction data
def generate_data(num_rows=1000):
    data = []
    for _ in range(num_rows):
        data.append({
            "transaction_id": faker.uuid4(),
            "user_id": faker.user_name(),
            "product": random.choice(["Laptop", "Phone", "Tablet", "Headphones", "Charger"]),
            "price": round(random.uniform(50, 1500), 2),
            "purchase_date": faker.date_between(start_date="-1y", end_date="today").strftime('%Y-%m-%d'),
            "location": faker.city(),
            "payment_method": random.choice(["Credit Card", "PayPal", "Crypto", "Bank Transfer"]),
        })
    
    return pd.DataFrame(data)

# Save as CSV
#df = generate_data(20000)
#df.to_parquet("synthetic_faker_transactions_20K.parquet", engine="pyarrow", index=False)

#df = generate_data(200000)
#df.to_parquet("synthetic_faker_transactions_200K.parquet", engine="pyarrow", index=False)

#df = generate_data(2000000)
#df.to_parquet("synthetic_faker_transactions_2M.parquet", engine="pyarrow", index=False)

#df = generate_data(200000000)
#df.to_parquet("synthetic_faker_transactions_20M.parquet", engine="pyarrow", index=False)

#df.to_csv("synthetic_faker_transactions.csv", index=False)
