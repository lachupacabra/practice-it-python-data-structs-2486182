# Practice It #26: Sessionize Web Events

Sessionization is a common analytics pipeline task.

Read `data/WebEvents.csv`, sort events per user, and split a user's activity into sessions. Start a new session when the gap between events is more than 30 minutes.

Return session records with user ID, session ID, start time, end time, and event count.

## Example Run
```console
python "src/26 Sessionize Web Events/solve.py"
```
