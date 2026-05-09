from collections import namedtuple
from csv import DictReader
from pprint import pprint


Customer = namedtuple("Customer", ["customer_id", "full_name", "email", "email_domain", "zipcode"])
OrderItem = namedtuple("OrderItem", ["order_item_id", "order_id", "product_id", "quantity"])


def read_customers(path):
    customers = []
    with open(path, "r") as open_csv:
        reader = DictReader(open_csv)
        for row in reader:
            email = row["Email"]
            customers.append(
                Customer(
                    customer_id=int(row["CustomerID"]),
                    full_name=f"{row['FirstName']} {row['LastName']}",
                    email=email,
                    email_domain=email.split("@")[-1],
                    zipcode=row["Zipcode"],
                )
            )
    return customers


def read_order_items(path):
    order_items = []
    with open(path, "r") as open_csv:
        reader = DictReader(open_csv)
        for row in reader:
            order_items.append(
                OrderItem(
                    order_item_id=row["OrderItemID"],
                    order_id=int(row["OrderID"]),
                    product_id=row["ProductID"],
                    quantity=int(row["Quantity"]),
                )
            )
    return order_items


def get_total_quantity_by_product(order_items):
    totals = {}
    for item in order_items:
        totals[item.product_id] = totals.get(item.product_id, 0) + item.quantity
    return totals


def main():
    customers = read_customers("data/Customer.csv")
    order_items = read_order_items("data/OrderItems.csv")

    pprint(customers[:3])
    pprint(order_items[:3])
    pprint(get_total_quantity_by_product(order_items))
    return


if __name__ == "__main__":
    main()
