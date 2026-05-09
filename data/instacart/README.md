# Instacart Practice Data

Download the full Instacart Market Basket Analysis CSV files from Kaggle and place them in:

```text
data/instacart/raw/
```

Expected raw files:

```text
aisles.csv
departments.csv
orders.csv
products.csv
order_products__prior.csv
order_products__train.csv
```

The notebook `05_instacart_postgres_data_engineering.ipynb` generates synthetic driver and delivery practice data in:

```text
data/instacart/generated/
```

Those generated files are for SQL/data-engineering practice only. The public Instacart market basket dataset contains order, product, aisle, department, and reorder history data, but it does not include real driver or delivery-route records.
