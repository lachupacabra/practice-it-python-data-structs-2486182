from collections import defaultdict, namedtuple
from pprint import pprint


OrderLine = namedtuple(
    "OrderLine",
    ["order_item_id", "order_id", "customer_id", "product_id", "quantity"],
)

ORDER_LINES = [
    OrderLine("I001", 1001, 100, "STA001", 2),
    OrderLine("I002", 1001, 100, "ENT004", 1),
    OrderLine("I003", 1002, 100, "DES005", 12),
    OrderLine("I003", 1002, 100, "DES005", 3),
    OrderLine("I004", 1003, 101, "BAD999", 1),
    OrderLine("I005", 1004, 102, "BEV003", 0),
    OrderLine("I006", 1005, 103, "SAL002", -2),
]

KNOWN_PREFIXES = {"STA", "BEV", "SAL", "ENT", "DES"}


def audit_order_lines(lines, known_prefixes):
    anomalies = defaultdict(list)
    quantities_by_product = defaultdict(int)
    seen_order_item_ids = set()

    for line in lines:
        if line.order_item_id in seen_order_item_ids:
            anomalies["duplicate_order_item_id"].append(line)
        else:
            seen_order_item_ids.add(line.order_item_id)

        if line.quantity <= 0:
            anomalies["non_positive_quantity"].append(line)

        if line.product_id[:3] not in known_prefixes:
            anomalies["unknown_product_prefix"].append(line)

        if line.quantity > 10:
            anomalies["unusually_large_quantity"].append(line)

        if line.quantity > 0 and line.product_id[:3] in known_prefixes:
            quantities_by_product[line.product_id] += line.quantity

    return {
        "anomalies": dict(anomalies),
        "quantities_by_product": dict(quantities_by_product),
    }


def main():
    pprint(audit_order_lines(ORDER_LINES, KNOWN_PREFIXES))
    return


if __name__ == "__main__":
    main()
