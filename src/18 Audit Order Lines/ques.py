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
    # TODO:
    # Use defaultdict(list) to group bad records by anomaly reason.
    # Use defaultdict(int) to aggregate valid quantities by product.
    #
    # Detect these anomaly reasons:
    # duplicate_order_item_id, non_positive_quantity, unknown_product_prefix,
    # unusually_large_quantity for quantities greater than 10.
    #
    # Return:
    # {
    #   "anomalies": normal dict of reason -> list of OrderLine records,
    #   "quantities_by_product": normal dict of product_id -> quantity
    # }
    aggs = defaultdict(int)
    errors = defaultdict(list)
    order_item_ids = []
    for line in lines:
        if line.order_item_id in order_item_ids:
            errors["duplicate_order_item_id"].append(line)
        elif line.quantity <=0:
            errors["non_positive_quantity"].append(line)
        elif line.product_id[:3] not in KNOWN_PREFIXES:
            errors["unknown_product_prefix"].append(line)
        elif line.quantity >10:
            errors["unusually_large_quantity"].append(line)
            aggs[line.product_id] += line.quantity
        else:
            aggs[line.product_id] += line.quantity
        order_item_ids.append(line.order_item_id)

    return {"anomalies": dict(errors),
            "quantities_by_product": dict(aggs)}


def main():
    pprint(audit_order_lines(ORDER_LINES, KNOWN_PREFIXES))
    return


if __name__ == "__main__":
    main()
