import json
from pathlib import Path
from pprint import pprint


def read_products(path):
    # TODO:
    # Read one JSON object per line from ProductCatalog.ndjson.
    return []


def flatten_catalog(products):
    # TODO:
    # Return one row per product price.
    # Include ProductID, ProductName, Department, Aisle, Brand, Organic, StoreID, Price.
    return []


def main():
    data_path = Path(__file__).resolve().parents[2] / "data/ProductCatalog.ndjson"
    products = read_products(data_path)

    pprint(flatten_catalog(products))
    return


if __name__ == "__main__":
    main()
