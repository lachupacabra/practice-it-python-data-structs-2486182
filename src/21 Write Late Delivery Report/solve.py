from csv import DictReader, DictWriter
from datetime import datetime
from pathlib import Path


REPORT_FIELDS = ["DeliveryID", "OrderID", "DriverID", "MinutesLate"]


def get_late_delivery_rows(source_path):
    late_rows = []

    with open(source_path, "r", newline="") as open_csv:
        reader = DictReader(open_csv)
        for row in reader:
            promised_by = datetime.fromisoformat(row["PromisedBy"])
            delivered_at = datetime.fromisoformat(row["DeliveredAt"])

            if delivered_at > promised_by:
                minutes_late = int((delivered_at - promised_by).total_seconds() // 60)
                late_rows.append(
                    {
                        "DeliveryID": row["DeliveryID"],
                        "OrderID": row["OrderID"],
                        "DriverID": row["DriverID"],
                        "MinutesLate": minutes_late,
                    }
                )

    return late_rows


def write_late_delivery_report(rows, output_path):
    with open(output_path, "w", newline="") as open_csv:
        writer = DictWriter(open_csv, fieldnames=REPORT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


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
