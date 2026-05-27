from collections import namedtuple
from csv import DictReader
from datetime import datetime
from pathlib import Path
from pprint import pprint


ChangeRecord = namedtuple(
    "ChangeRecord",
    ["change_id", "customer_id", "operation", "updated_at", "email"],
)


def read_change_log(path):
    changes = []

    with open(path, "r", newline="") as open_csv:
        reader = DictReader(open_csv)
        for row in reader:
            changes.append(
                ChangeRecord(
                    change_id=row["ChangeID"],
                    customer_id=row["CustomerID"],
                    operation=row["Operation"],
                    updated_at=datetime.fromisoformat(row["UpdatedAt"]),
                    email=row["Email"],
                )
            )

    return changes


def get_changes_after_watermark(changes, last_watermark):
    loaded_changes = [
        change for change in changes if change.updated_at > last_watermark
    ]
    return sorted(loaded_changes, key=lambda change: change.updated_at)


def get_next_watermark(loaded_changes, current_watermark):
    if not loaded_changes:
        return current_watermark

    return max(change.updated_at for change in loaded_changes)


def main():
    data_path = Path(__file__).resolve().parents[2] / "data/CustomerChangeLog.csv"
    last_watermark = datetime.fromisoformat("2026-05-01T09:30:00")

    changes = read_change_log(data_path)
    loaded_changes = get_changes_after_watermark(changes, last_watermark)

    pprint(loaded_changes)
    pprint(get_next_watermark(loaded_changes, last_watermark))
    return


if __name__ == "__main__":
    main()
