from collections import defaultdict, namedtuple
from pprint import pprint


OrderLine = namedtuple("OrderLine", ["customer_id", "order_id", "product_id", "quantity"])

ORDER_LINES = [
    OrderLine(100, 1001, "STA001", 2),
    OrderLine(100, 1001, "ENT004", 1),
    OrderLine(100, 1002, "DES005", 3),
    OrderLine(101, 1003, "BEV003", 2),
    OrderLine(101, 1003, "DES005", 1),
    OrderLine(102, 1004, "SAL002", 4),
    OrderLine(102, 1005, "ENT001", 2),
]

CATEGORY_NAMES = {
    "STA": "starter",
    "BEV": "beverage",
    "SAL": "salad",
    "ENT": "entree",
    "DES": "dessert",
}


def get_category(product_id):
    # TODO:
    # Return a human-readable category from the first three letters
    # of product_id. Return "unknown" when the prefix is missing.
    return ""


def group_quantities(lines):
    # TODO:
    # Use nested defaultdict objects to build:
    # customer_id -> order_id -> category -> total quantity.
    # Return a regular dict when done.
    return {}


def main():
    pprint(group_quantities(ORDER_LINES))
    return


if __name__ == "__main__":
    main()
