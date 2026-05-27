from collections import defaultdict, namedtuple
from csv import DictReader
from datetime import datetime, timedelta
from pathlib import Path
from pprint import pprint


WebEvent = namedtuple("WebEvent", ["user_id", "event_time", "event_name"])
Session = namedtuple("Session", ["user_id", "session_id", "start_time", "end_time", "event_count"])


def read_web_events(path):
    events = []

    with open(path, "r", newline="") as open_csv:
        reader = DictReader(open_csv)
        for row in reader:
            events.append(
                WebEvent(
                    user_id=row["UserID"],
                    event_time=datetime.fromisoformat(row["EventTime"]),
                    event_name=row["EventName"],
                )
            )

    return events


def sessionize_events(events, inactivity_minutes=30):
    events_by_user = defaultdict(list)
    sessions = []
    inactivity_gap = timedelta(minutes=inactivity_minutes)

    for event in events:
        events_by_user[event.user_id].append(event)

    for user_id in sorted(events_by_user):
        user_events = sorted(events_by_user[user_id], key=lambda event: event.event_time)
        session_number = 1
        start_time = user_events[0].event_time
        end_time = user_events[0].event_time
        event_count = 1

        for event in user_events[1:]:
            if event.event_time - end_time > inactivity_gap:
                sessions.append(
                    Session(
                        user_id=user_id,
                        session_id=f"{user_id}-{session_number}",
                        start_time=start_time,
                        end_time=end_time,
                        event_count=event_count,
                    )
                )
                session_number += 1
                start_time = event.event_time
                event_count = 0

            end_time = event.event_time
            event_count += 1

        sessions.append(
            Session(
                user_id=user_id,
                session_id=f"{user_id}-{session_number}",
                start_time=start_time,
                end_time=end_time,
                event_count=event_count,
            )
        )

    return sessions


def main():
    data_path = Path(__file__).resolve().parents[2] / "data/WebEvents.csv"
    events = read_web_events(data_path)

    pprint(sessionize_events(events, inactivity_minutes=30))
    return


if __name__ == "__main__":
    main()
