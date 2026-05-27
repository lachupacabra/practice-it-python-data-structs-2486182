from collections import defaultdict, namedtuple
from csv import DictReader
from pathlib import Path
from pprint import pprint


CustomerAccount = namedtuple("CustomerAccount", ["customer_id", "full_name", "email", "segment"])
Order = namedtuple("Order", ["order_id", "customer_id", "order_total", "order_status"])


def read_customers(path):
    # TODO:
    # Read CustomerAccounts.csv with DictReader.
    # Return CustomerAccount records.
    return []


def read_orders(path):
    # TODO:
    # Read OrdersForJoin.csv with DictReader.
    # Convert OrderTotal to float and return Order records.
    return []


def join_orders_to_customers(orders, customers):
    # TODO:
    # Join each order to its customer by customer_id.
    # Return dictionaries and include missing_customer as True or False.
    return []


def revenue_by_segment(joined_orders):
    # TODO:
    # Sum completed order revenue by segment.
    # Put missing customers in an "UNKNOWN" segment.
    return {}


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
