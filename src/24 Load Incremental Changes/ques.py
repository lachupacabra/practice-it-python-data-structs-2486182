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
    # TODO:
    # Read CustomerChangeLog.csv with DictReader.
    # Convert UpdatedAt to a datetime object.
    return []


def get_changes_after_watermark(changes, last_watermark):
    # TODO:
    # Return changes with updated_at later than last_watermark, sorted by updated_at.
    return []


def get_next_watermark(loaded_changes, current_watermark):
    # TODO:
    # Return the max updated_at from loaded_changes, or current_watermark if none loaded.
    return current_watermark


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
