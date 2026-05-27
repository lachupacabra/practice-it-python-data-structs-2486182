from csv import DictReader
from datetime import date
from pathlib import Path
from pprint import pprint


ALLOWED_STATUSES = {"completed", "canceled", "refunded"}
REQUIRED_FIELDS = ["OrderID", "CustomerID", "OrderTotal", "Status", "OrderDate"]


def read_raw_orders(path):
    # TODO:
    # Read RawOrderRows.csv with DictReader.
    # Add a _row_number value to each row so errors can point back to the file.
    return []


def validate_order_rows(rows):
    # TODO:
    # Return {"valid_rows": [...], "error_rows": [...]}.
    # Valid rows should have typed order_total and order_date values.
    # Error rows should include row_number, row, and errors.
    return {"valid_rows": [], "error_rows": []}


def main():
    data_path = Path(__file__).resolve().parents[2] / "data/RawOrderRows.csv"
    rows = read_raw_orders(data_path)

    pprint(validate_order_rows(rows))
    return


if __name__ == "__main__":
    main()
