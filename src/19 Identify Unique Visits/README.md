# Practice It #19: Identify Unique Visits

Read `data/PlaceDeviceReadings.csv` and identify unique visits from repeated place/device observations.

Each CSV row has a `PlaceID`, `DeviceID`, and `RecordedAt` timestamp. A place/device pair can appear many times because the device was recorded more than once. For this exercise, one unique visit is one `PlaceID` + `DeviceID` pair in the file.

Implement helpers to read the CSV with `DictReader`, parse timestamps, summarize each unique visit with its first timestamp, last timestamp, and observation count, then count unique visits by place.

## Example Run
```console
python "src/19 Identify Unique Visits/solve.py"
```
