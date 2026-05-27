from csv import DictReader, DictWriter
from datetime import datetime
from pathlib import Path


REPORT_FIELDS = ["DeliveryID", "OrderID", "DriverID", "MinutesLate"]


def get_late_delivery_rows(source_path):
    # TODO:
    # Read DeliveryPerformance.csv with DictReader.
    # Return dictionaries with REPORT_FIELDS for late deliveries only.
    return []


def write_late_delivery_report(rows, output_path):
    # TODO:
    # Use DictWriter to write the header and rows to output_path.
    return


def main():
    exercise_dir = Path(__file__).resolve().parent
    data_path = exercise_dir.parents[1] / "data/DeliveryPerformance.csv"
    output_path = exercise_dir / "late_delivery_report.csv"

    rows = get_late_delivery_rows(data_path)
    write_late_delivery_report(rows, output_path)

    print(output_path)
    return


if __name__ == "__main__":
    main()
