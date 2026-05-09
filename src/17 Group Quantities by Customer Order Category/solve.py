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
    return CATEGORY_NAMES.get(product_id[:3], "unknown")


def freeze_grouped_quantities(grouped):
    return {
        customer_id: {
            order_id: dict(category_totals)
            for order_id, category_totals in orders.items()
        }
        for customer_id, orders in grouped.items()
    }


def group_quantities(lines):
    grouped = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    for line in lines:
        category = get_category(line.product_id)
        grouped[line.customer_id][line.order_id][category] += line.quantity

    return freeze_grouped_quantities(grouped)


def main():
    pprint(group_quantities(ORDER_LINES))
    return


if __name__ == "__main__":
    main()
