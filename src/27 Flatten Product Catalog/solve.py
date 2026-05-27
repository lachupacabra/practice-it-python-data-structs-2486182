import json
from pathlib import Path
from pprint import pprint


def read_products(path):
    products = []

    with open(path, "r") as open_file:
        for line in open_file:
            products.append(json.loads(line))

    return products


def flatten_catalog(products):
    rows = []

    for product in products:
        category = product.get("category", {})
        attributes = product.get("attributes", {})

        for price in product.get("prices", []):
            rows.append(
                {
                    "ProductID": product["product_id"],
                    "ProductName": product["name"],
                    "Department": category.get("department"),
                    "Aisle": category.get("aisle"),
                    "Brand": attributes.get("brand"),
                    "Organic": attributes.get("organic", False),
                    "StoreID": price["store_id"],
                    "Price": price["price"],
                }
            )

    return rows


def main():
    data_path = Path(__file__).resolve().parents[2] / "data/ProductCatalog.ndjson"
    products = read_products(data_path)

    pprint(flatten_catalog(products))
    return


if __name__ == "__main__":
    main()
