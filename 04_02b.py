from collections import namedtuple,defaultdict
from csv import reader
from pprint import pprint

def read_data(loc):
    res = defaultdict(int)
    with open(loc,'r') as file:
        read = reader(file)
        Order = namedtuple('Order',next(read))
        for row in read:
            order = Order(*row)
            res[order.ProductID] += int(order.Quantity)
    return res

def main():
    # add code here
    pprint(dict(read_data("data/OrderItems.csv")))

    return

if __name__ == "__main__":
    main()
