from collections import namedtuple
from datetime import datetime
from pprint import pprint


DeliveryEvent = namedtuple("DeliveryEvent", ["delivery_id", "status", "timestamp"])

RAW_EVENTS = [
    ("D1001", "accepted", "2026-04-28T09:00:00"),
    ("D1001", "shopping_started", "2026-04-28T09:08:00"),
    ("D1001", "checked_out", "2026-04-28T09:36:00"),
    ("D1001", "delivered", "2026-04-28T10:10:00"),
    ("D1002", "accepted", "2026-04-28T09:15:00"),
    ("D1002", "delivered", "2026-04-28T09:55:00"),
    ("D1002", "out_for_delivery", "2026-04-28T10:05:00"),
    ("D1003", "accepted", "2026-04-28T11:00:00"),
    ("D1003", "canceled", "2026-04-28T11:05:00"),
    ("D1003", "shopping_started", "2026-04-28T11:12:00"),
]

STATUS_RANK = {
    "accepted": 1,
    "shopping_started": 2,
    "checked_out": 3,
    "out_for_delivery": 4,
    "delivered": 5,
    "canceled": 5,
}


def parse_event(raw_event):
    # TODO:
    # Convert a tuple like ("D1001", "accepted", "2026-04-28T09:00:00")
    # into a DeliveryEvent with a datetime timestamp.
    return None


def find_invalid_transitions(events):
    # TODO:
    # Validate event order within each delivery_id.
    # Return a list of dictionaries describing invalid transitions.
    # A status is invalid if it moves backward in STATUS_RANK or happens
    # after delivered/canceled.
    return []


def update_status(event, new_status):
    # TODO:
    # namedtuple records are immutable, so return a copy with _replace.
    return event


def main():
    events = [parse_event(raw_event) for raw_event in RAW_EVENTS]
    pprint(events[:3])
    pprint(find_invalid_transitions(events))
    pprint(update_status(events[0], "shopping_started"))
    return


if __name__ == "__main__":
    main()
