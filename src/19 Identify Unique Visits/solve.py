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
    records = []

    with open(path, "r", newline="") as open_csv:
        reader = DictReader(open_csv)
        for row in reader:
            records.append(
                VisitRecord(
                    place_id=row["PlaceID"],
                    device_id=row["DeviceID"],
                    recorded_at=datetime.fromisoformat(row["RecordedAt"]),
                )
            )

    return records


def get_unique_visits(records):
    visits = {}

    for record in records:
        key = (record.place_id, record.device_id)

        if key not in visits:
            visits[key] = {
                "first_seen": record.recorded_at,
                "last_seen": record.recorded_at,
                "observation_count": 0,
            }

        visit = visits[key]
        visit["first_seen"] = min(visit["first_seen"], record.recorded_at)
        visit["last_seen"] = max(visit["last_seen"], record.recorded_at)
        visit["observation_count"] += 1

    unique_visits = []
    for place_id, device_id in sorted(visits):
        visit = visits[(place_id, device_id)]
        unique_visits.append(
            UniqueVisit(
                place_id=place_id,
                device_id=device_id,
                first_seen=visit["first_seen"],
                last_seen=visit["last_seen"],
                observation_count=visit["observation_count"],
            )
        )

    return unique_visits


def count_unique_visits_by_place(unique_visits):
    counts = defaultdict(int)

    for visit in unique_visits:
        counts[visit.place_id] += 1

    return dict(counts)


def main():
    data_path = Path(__file__).resolve().parents[2] / "data/PlaceDeviceReadings.csv"

    records = read_visit_records(data_path)
    unique_visits = get_unique_visits(records)

    pprint(unique_visits)
    pprint(count_unique_visits_by_place(unique_visits))
    return


if __name__ == "__main__":
    main()
