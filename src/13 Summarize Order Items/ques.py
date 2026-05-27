from collections import namedtuple, Counter
from csv import DictReader
from pprint import pprint
from pathlib import Path

Customer = namedtuple(
    "Customer", ["customer_id", "full_name", "email", "email_domain", "zipcode"]
)
OrderItem = namedtuple(
    "OrderItem", ["order_item_id", "order_id", "product_id", "quantity"]
)


def read_customers(path):
    # TODO:
    # Read Customer.csv with DictReader.
    # Return a list of Customer records.
    # Convert CustomerID to int and build full_name from FirstName + LastName.
    ans = []
    with open(path, "r") as file:
        reader = DictReader(file)
        for row in reader:
            customer_id = int(row["CustomerID"])
            first_name = row["FirstName"]
            last_name = row["LastName"]
            full_name = first_name + " " + last_name
            email = row["Email"]
            email_domain = email[email.find("@") + 1 :]
            zipcode = row["Zipcode"]
            customer = Customer(customer_id, full_name, email, email_domain, zipcode)
            ans.append(customer)
    return ans


def read_order_items(path):
    # TODO:
    # Read OrderItems.csv with DictReader.
    # Return a list of OrderItem records.
    # Convert OrderID and Quantity to int.
    ans = []
    with open(path, "r") as file:
        reader = DictReader(file)
        for row in reader:
            orderItemId = row["OrderItemID"]
            orderId = int(row["OrderID"])
            productId = row["ProductID"]
            quantity = int(row["Quantity"])
            orderItem = OrderItem(orderItemId, orderId, productId, quantity)
            ans.append(orderItem)
    return ans


def get_total_quantity_by_product(order_items):
    # TODO:
    # Use the product_id and quantity fields from each OrderItem.
    # Return a normal dictionary of product_id -> total quantity.
    counts = Counter()
    for item in order_items:
        counts[item.product_id] += item.quantity
    return dict(counts)


def main():
    current_dir = Path(__file__).resolve().parent

    # print(current_dir.parent)
    csv_dir = current_dir.parent.parent
    customers = read_customers(csv_dir / "data/Customer.csv")
    order_items = read_order_items(csv_dir / "data/OrderItems.csv")

    pprint(customers[:3])
    pprint(order_items[:3])
    pprint(get_total_quantity_by_product(order_items))
    return


if __name__ == "__main__":
    main()
