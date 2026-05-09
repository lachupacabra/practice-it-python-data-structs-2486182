from collections import Counter, deque, namedtuple
from pprint import pprint


OrderEvent = namedtuple("OrderEvent", ["event_id", "customer_id", "product_id"])

ORDER_EVENTS = [
    OrderEvent("E001", 101, "BANANA"),
    OrderEvent("E002", 102, "APPLE"),
    OrderEvent("E003", 103, "BANANA"),
    OrderEvent("E004", 104, "YOGURT"),
    OrderEvent("E005", 105, "BANANA"),
    OrderEvent("E006", 106, "BASIL"),
    OrderEvent("E007", 107, "APPLE"),
    OrderEvent("E008", 108, "BANANA"),
    OrderEvent("E009", 109, "APPLE"),
    OrderEvent("E010", 110, "APPLE"),
]


def rolling_product_alerts(events, window_size=6, surge_threshold=3):
    window = deque(maxlen=window_size)
    product_counts = Counter()
    alerts = []

    for event in events:
        if len(window) == window.maxlen:
            removed_event = window[0]
            product_counts[removed_event.product_id] -= 1
            if product_counts[removed_event.product_id] == 0:
                del product_counts[removed_event.product_id]

        window.append(event)
        product_counts[event.product_id] += 1

        if product_counts[event.product_id] >= surge_threshold:
            alerts.append(
                {
                    "event_id": event.event_id,
                    "product_id": event.product_id,
                    "count_in_window": product_counts[event.product_id],
                    "recent_event_ids": [recent.event_id for recent in window],
                }
            )

    return alerts


def main():
    pprint(rolling_product_alerts(ORDER_EVENTS, window_size=6, surge_threshold=3))
    return


if __name__ == "__main__":
    main()
