from collections import namedtuple
from csv import DictReader
from pprint import pprint


Customer = namedtuple("Customer", ["customer_id", "full_name", "email", "email_domain", "zipcode"])
OrderItem = namedtuple("OrderItem", ["order_item_id", "order_id", "product_id", "quantity"])


def read_customers(path):
    # TODO:
    # Read Customer.csv with DictReader.
    # Return a list of Customer records.
    # Convert CustomerID to int and build full_name from FirstName + LastName.
    return []


def read_order_items(path):
    # TODO:
    # Read OrderItems.csv with DictReader.
    # Return a list of OrderItem records.
    # Convert OrderID and Quantity to int.
    return []


def get_total_quantity_by_product(order_items):
    # TODO:
    # Use the product_id and quantity fields from each OrderItem.
    # Return a normal dictionary of product_id -> total quantity.
    return {}


def main():
    customers = read_customers("data/Customer.csv")
    order_items = read_order_items("data/OrderItems.csv")

    pprint(customers[:3])
    pprint(order_items[:3])
    pprint(get_total_quantity_by_product(order_items))
    return


if __name__ == "__main__":
    main()
