from collections import defaultdict, namedtuple
from csv import DictReader
from datetime import datetime
from pathlib import Path
from pprint import pprint


VisitRecord = namedtuple("VisitRecord", ["place_id", "device_id", "recorded_at"])
UniqueVisit = namedtuple(
    "UniqueVisit",
    ["place_id", "device_id", "first_seen", "last_seen", "observation_count"],
)


def read_visit_records(path):
    # TODO:
    # Read PlaceDeviceReadings.csv with DictReader.
    # Return VisitRecord objects and convert RecordedAt to a datetime.
    return []


def get_unique_visits(records):
    # TODO:
    # A unique visit is one place_id + device_id pair.
    # Return UniqueVisit records with first_seen, last_seen, and observation_count.
    return []


def count_unique_visits_by_place(unique_visits):
    # TODO:
    # Count how many unique visits each place had.
    # Return a normal dictionary of place_id -> unique visit count.
    return {}


def main():
    data_path = Path(__file__).resolve().parents[2] / "data/PlaceDeviceReadings.csv"

    records = read_visit_records(data_path)
    unique_visits = get_unique_visits(records)

    pprint(unique_visits)
    pprint(count_unique_visits_by_place(unique_visits))
    return


if __name__ == "__main__":
    main()
