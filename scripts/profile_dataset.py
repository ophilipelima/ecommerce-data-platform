from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/raw")

# Verificar unicidade
for file in DATA_PATH.glob("*csv"):

    df = pd.read_csv(file)

    print(f"{df.columns[0]}: {df[df.columns[0]].is_unique}")

# Verificar integridade referencial das tabelas

customers_df = pd.read_csv("data/raw/olist_customers_dataset.csv")
orders_df = pd.read_csv("data/raw/olist_customers_dataset.csv")

print(orders_df["customer_id"].isin(customers_df["customer_id"]).all())

order_itens_df = pd.read_csv("olist_order_items_dataset.csv")
products_df = pd.read_csv("olist_products_dataset.csv")

print(order_itens_df["product_id"].isin(products_df["products_df"]).all())


