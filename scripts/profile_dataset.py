from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/raw")

# Verificar unicidade
for file in DATA_PATH.glob("*csv"):

    chaves_compostas = {
              "data/raw/olist_order_items_dataset.csv": ["order_id","order_item_id"], 
              "data/raw/olist_order_payments_dataset.csv": ["order_id","payment_sequential"]          
              }
    
    df = pd.read_csv(file)

    print(f"\nTabela: {file}")
    for file_chave_composta in chaves_compostas.keys():
        if file_chave_composta == file: 
            print(f"{df.columns[[file_chave_composta[0], [1]]]}: {df[df.columns[file_chave_composta[0], [1]]].is_unique()}")
            break

    if file not in chaves_compostas.keys():
        print(f"{df.columns[0]}: {df[df.columns[0]].is_unique}")

# Verificar integridade referencial das tabelas

customers_df = pd.read_csv("data/raw/olist_customers_dataset.csv")
orders_df = pd.read_csv("data/raw/olist_orders_dataset.csv")
order_items_df = pd.read_csv("data/raw/olist_order_items_dataset.csv")
products_df = pd.read_csv("data/raw/olist_products_dataset.csv")
sallers_df = pd.read_csv("data/raw/olist_sellers_dataset.csv")
payments_df = pd.read_csv("data/raw/olist_order_payments_dataset.csv")

print("\nIntegridade Pedidos -> Cliente:")
print(orders_df["customer_id"].isin(customers_df["customer_id"]).all())

print("\nIntegridade Itens de pedidos -> Produtos:")
print(order_items_df["product_id"].isin(products_df["product_id"]).all())

print("\nIntegridade Vendedor(em items) -> Vendedores ")
print(order_items_df["seller_id"].isin(sallers_df["seller_id"]).all())

print("\nIntegridade Pedido -> Itens de pedido")
print(orders_df["order_id"].isin(order_items_df["order_id"]).all())

orders_without_items = orders_df[orders_df["order_id"].isin(order_items_df["order_id"])]

print(orders_without_items["order_status"].value_counts())

# GRANULARIDADE

# Quantos itens existem, em média, por pedido?

qtdPedidos = len(orders_df)
qtdItens = order_items_df["order_id"].value_counts().sum()
mediaItens = qtdItens / qtdPedidos

print(f"\nMedia de itens por pedido: {mediaItens}")

# Quantos pagamentos existem, em média, por pedido?

qtdPagamentos  = payments_df["order_id"].value_counts().sum()
mediaPagamentos = qtdPagamentos / qtdPedidos
print(f"\nMedia de pagamentos por pedido: {mediaPagamentos}")

# Quantidade de itens por pedido
itens_por_pedido = (order_items_df.groupby("order_id").size())

print("\nDistribuição de itens por pedido:")
print(itens_por_pedido.describe())

print("Pedidos com mais de um item:",(itens_por_pedido > 1).sum())

print("Máximo de itens em um pedido:",itens_por_pedido.max())
