from csv import DictReader
from datetime import date
from pathlib import Path
from pprint import pprint


ALLOWED_STATUSES = {"completed", "canceled", "refunded"}
REQUIRED_FIELDS = ["OrderID", "CustomerID", "OrderTotal", "Status", "OrderDate"]


def read_raw_orders(path):
    rows = []

    with open(path, "r", newline="") as open_csv:
        reader = DictReader(open_csv)
        for row_number, row in enumerate(reader, start=2):
            row["_row_number"] = row_number
            rows.append(row)

    return rows


def validate_order_rows(rows):
    valid_rows = []
    error_rows = []

    for row in rows:
        errors = []

        for field in REQUIRED_FIELDS:
            if not row.get(field):
                errors.append(f"missing_{field}")

        order_total = None
        if row.get("OrderTotal"):
            try:
                order_total = float(row["OrderTotal"])
                if order_total <= 0:
                    errors.append("non_positive_order_total")
            except ValueError:
                errors.append("invalid_order_total")

        order_date = None
        if row.get("OrderDate"):
            try:
                order_date = date.fromisoformat(row["OrderDate"])
            except ValueError:
                errors.append("invalid_order_date")

        if row.get("Status") and row["Status"] not in ALLOWED_STATUSES:
            errors.append("invalid_status")

        if errors:
            error_rows.append(
                {
                    "row_number": row["_row_number"],
                    "row": row,
                    "errors": errors,
                }
            )
        else:
            valid_rows.append(
                {
                    "order_id": row["OrderID"],
                    "customer_id": row["CustomerID"],
                    "order_total": order_total,
                    "status": row["Status"],
                    "order_date": order_date,
                }
            )

    return {"valid_rows": valid_rows, "error_rows": error_rows}


def main():
    data_path = Path(__file__).resolve().parents[2] / "data/RawOrderRows.csv"
    rows = read_raw_orders(data_path)

    pprint(validate_order_rows(rows))
    return


if __name__ == "__main__":
    main()
