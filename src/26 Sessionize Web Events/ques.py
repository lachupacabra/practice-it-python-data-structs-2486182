from collections import defaultdict, namedtuple
from csv import DictReader
from datetime import datetime, timedelta
from pathlib import Path
from pprint import pprint


WebEvent = namedtuple("WebEvent", ["user_id", "event_time", "event_name"])
Session = namedtuple("Session", ["user_id", "session_id", "start_time", "end_time", "event_count"])


def read_web_events(path):
    # TODO:
    # Read WebEvents.csv with DictReader and convert EventTime to datetime.
    return []


def sessionize_events(events, inactivity_minutes=30):
    # TODO:
    # Group events by user and sort by event_time.
    # Start a new session when the time gap is greater than inactivity_minutes.
    return []


def main():
    data_path = Path(__file__).resolve().parents[2] / "data/WebEvents.csv"
    events = read_web_events(data_path)

    pprint(sessionize_events(events, inactivity_minutes=30))
    return


if __name__ == "__main__":
    main()
