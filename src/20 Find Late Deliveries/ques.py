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
    # TODO:
    # Read DeliveryPerformance.csv with DictReader.
    # Convert PromisedBy and DeliveredAt to datetime objects.
    return []


def find_late_deliveries(events):
    # TODO:
    # Return dictionaries for deliveries where delivered_at is after promised_by.
    # Include delivery_id, order_id, driver_id, and minutes_late.
    return []


def count_late_deliveries_by_driver(late_deliveries):
    # TODO:
    # Return a normal dictionary of driver_id -> late delivery count.
    return {}


def main():
    data_path = Path(__file__).resolve().parents[2] / "data/DeliveryPerformance.csv"

    events = read_delivery_events(data_path)
    late_deliveries = find_late_deliveries(events)

    pprint(late_deliveries)
    pprint(count_late_deliveries_by_driver(late_deliveries))
    return


if __name__ == "__main__":
    main()
