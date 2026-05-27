from csv import reader
from collections import namedtuple

from pathlib import Path
from pprint import pprint

# Get the directory of the current script


def main():
    # add code here
    # read data/Customer.csv
    # Create workable objects with each line
    current_dir = Path(__file__).resolve().parent

    # print(current_dir.parent)
    csv_dir = current_dir.parent.parent / "data" / "Customer.csv"
    ans = []
    with open(csv_dir, "r") as file:
        read = reader(file)
        Customer = namedtuple("Customer", next(read))
        for line in read:
            ans.append(Customer(*line))
    pprint(ans)
    return ans


if __name__ == "__main__":
    main()
