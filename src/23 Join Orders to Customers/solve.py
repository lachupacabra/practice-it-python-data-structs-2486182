from collections import defaultdict, namedtuple
from csv import DictReader
from pathlib import Path
from pprint import pprint


CustomerAccount = namedtuple("CustomerAccount", ["customer_id", "full_name", "email", "segment"])
Order = namedtuple("Order", ["order_id", "customer_id", "order_total", "order_status"])


def read_customers(path):
    customers = []

    with open(path, "r", newline="") as open_csv:
        reader = DictReader(open_csv)
        for row in reader:
            customers.append(
                CustomerAccount(
                    customer_id=row["CustomerID"],
                    full_name=row["FullName"],
                    email=row["Email"],
                    segment=row["Segment"],
                )
            )

    return customers


def read_orders(path):
    orders = []

    with open(path, "r", newline="") as open_csv:
        reader = DictReader(open_csv)
        for row in reader:
            orders.append(
                Order(
                    order_id=row["OrderID"],
                    customer_id=row["CustomerID"],
                    order_total=float(row["OrderTotal"]),
                    order_status=row["OrderStatus"],
                )
            )

    return orders


def join_orders_to_customers(orders, customers):
    customers_by_id = {customer.customer_id: customer for customer in customers}
    joined_orders = []

    for order in orders:
        customer = customers_by_id.get(order.customer_id)
        joined_orders.append(
            {
                "order_id": order.order_id,
                "customer_id": order.customer_id,
                "order_total": order.order_total,
                "order_status": order.order_status,
                "customer_name": customer.full_name if customer else None,
                "email": customer.email if customer else None,
                "segment": customer.segment if customer else None,
                "missing_customer": customer is None,
            }
        )

    return joined_orders


def revenue_by_segment(joined_orders):
    revenue = defaultdict(float)

    for order in joined_orders:
        if order["order_status"] == "completed":
            segment = order["segment"] or "UNKNOWN"
            revenue[segment] += order["order_total"]

    return dict(revenue)


def main():
    data_dir = Path(__file__).resolve().parents[2] / "data"
    customers = read_customers(data_dir / "CustomerAccounts.csv")
    orders = read_orders(data_dir / "OrdersForJoin.csv")
    joined_orders = join_orders_to_customers(orders, customers)

    pprint(joined_orders)
    pprint(revenue_by_segment(joined_orders))
    return


if __name__ == "__main__":
    main()
