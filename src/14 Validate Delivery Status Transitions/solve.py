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

TERMINAL_STATUSES = {"delivered", "canceled"}


def parse_event(raw_event):
    delivery_id, status, timestamp = raw_event
    return DeliveryEvent(
        delivery_id=delivery_id,
        status=status,
        timestamp=datetime.fromisoformat(timestamp),
    )


def find_invalid_transitions(events):
    invalid_transitions = []
    last_event_by_delivery = {}

    for event in sorted(events, key=lambda item: (item.delivery_id, item.timestamp)):
        previous_event = last_event_by_delivery.get(event.delivery_id)

        if previous_event is not None:
            previous_rank = STATUS_RANK[previous_event.status]
            current_rank = STATUS_RANK[event.status]

            if previous_event.status in TERMINAL_STATUSES:
                invalid_transitions.append(
                    {
                        "delivery_id": event.delivery_id,
                        "previous_status": previous_event.status,
                        "current_status": event.status,
                        "reason": "event_after_terminal_status",
                    }
                )
            elif current_rank < previous_rank:
                invalid_transitions.append(
                    {
                        "delivery_id": event.delivery_id,
                        "previous_status": previous_event.status,
                        "current_status": event.status,
                        "reason": "status_moved_backward",
                    }
                )

        last_event_by_delivery[event.delivery_id] = event

    return invalid_transitions


def update_status(event, new_status):
    return event._replace(status=new_status)


def main():
    events = [parse_event(raw_event) for raw_event in RAW_EVENTS]
    pprint(events[:3])
    pprint(find_invalid_transitions(events))
    pprint(update_status(events[0], "shopping_started"))
    return


if __name__ == "__main__":
    main()
