from collections import Counter, namedtuple
from csv import DictReader
from datetime import datetime
from pathlib import Path
from pprint import pprint


EventUpdate = namedtuple(
    "EventUpdate",
    ["event_id", "customer_id", "event_type", "event_time", "updated_at", "payload_version"],
)


def read_event_updates(path):
    # TODO:
    # Read EventUpdates.csv with DictReader.
    # Convert EventTime and UpdatedAt to datetime objects.
    # Convert PayloadVersion to int.
    return []


def deduplicate_latest_updates(updates):
    # TODO:
    # Keep only the row with the latest updated_at for each event_id.
    # Return the deduplicated EventUpdate records sorted by event_id.
    return []


def count_duplicate_updates(updates):
    # TODO:
    # Return event_id -> number of extra update rows for events with duplicates.
    return {}


def main():
    data_path = Path(__file__).resolve().parents[2] / "data/EventUpdates.csv"
    updates = read_event_updates(data_path)

    pprint(deduplicate_latest_updates(updates))
    pprint(count_duplicate_updates(updates))
    return


if __name__ == "__main__":
    main()
