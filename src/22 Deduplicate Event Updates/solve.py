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
    updates = []

    with open(path, "r", newline="") as open_csv:
        reader = DictReader(open_csv)
        for row in reader:
            updates.append(
                EventUpdate(
                    event_id=row["EventID"],
                    customer_id=row["CustomerID"],
                    event_type=row["EventType"],
                    event_time=datetime.fromisoformat(row["EventTime"]),
                    updated_at=datetime.fromisoformat(row["UpdatedAt"]),
                    payload_version=int(row["PayloadVersion"]),
                )
            )

    return updates


def deduplicate_latest_updates(updates):
    latest_by_event_id = {}

    for update in updates:
        current = latest_by_event_id.get(update.event_id)
        if current is None or update.updated_at > current.updated_at:
            latest_by_event_id[update.event_id] = update

    return [latest_by_event_id[event_id] for event_id in sorted(latest_by_event_id)]


def count_duplicate_updates(updates):
    counts = Counter(update.event_id for update in updates)
    return {event_id: count - 1 for event_id, count in counts.items() if count > 1}


def main():
    data_path = Path(__file__).resolve().parents[2] / "data/EventUpdates.csv"
    updates = read_event_updates(data_path)

    pprint(deduplicate_latest_updates(updates))
    pprint(count_duplicate_updates(updates))
    return


if __name__ == "__main__":
    main()
