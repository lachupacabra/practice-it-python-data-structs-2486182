from collections import defaultdict, namedtuple
from csv import DictReader
from datetime import datetime
from pathlib import Path
from pprint import pprint


DeliveryEvent = namedtuple(
    "DeliveryEvent",
    ["delivery_id", "order_id", "driver_id", "promised_by", "delivered_at"],
)


def read_delivery_events(path):
    events = []

    with open(path, "r", newline="") as open_csv:
        reader = DictReader(open_csv)
        for row in reader:
            events.append(
                DeliveryEvent(
                    delivery_id=row["DeliveryID"],
                    order_id=row["OrderID"],
                    driver_id=row["DriverID"],
                    promised_by=datetime.fromisoformat(row["PromisedBy"]),
                    delivered_at=datetime.fromisoformat(row["DeliveredAt"]),
                )
            )

    return events


def find_late_deliveries(events):
    late_deliveries = []

    for event in events:
        if event.delivered_at > event.promised_by:
            minutes_late = int(
                (event.delivered_at - event.promised_by).total_seconds() // 60
            )
            late_deliveries.append(
                {
                    "delivery_id": event.delivery_id,
                    "order_id": event.order_id,
                    "driver_id": event.driver_id,
                    "minutes_late": minutes_late,
                }
            )

    return late_deliveries


def count_late_deliveries_by_driver(late_deliveries):
    counts = defaultdict(int)

    for delivery in late_deliveries:
        counts[delivery["driver_id"]] += 1

    return dict(counts)


def main():
    data_path = Path(__file__).resolve().parents[2] / "data/DeliveryPerformance.csv"

    events = read_delivery_events(data_path)
    late_deliveries = find_late_deliveries(events)

    pprint(late_deliveries)
    pprint(count_late_deliveries_by_driver(late_deliveries))
    return


if __name__ == "__main__":
    main()
