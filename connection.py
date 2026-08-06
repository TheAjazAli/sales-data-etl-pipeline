import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv("cleaned_sales_data.csv")

# PostgreSQL Connection
engine = create_engine(
    "postgresql://postgres:Yourname@localhost:Password/Yourdatabse"
)

# Load into PostgreSQL
df.to_sql(
    'sales_data',
    con=engine,
    if_exists='replace',
    index=False
)

print("Data loaded successfully")