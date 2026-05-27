# Practice It #22: Deduplicate Event Updates

Data pipelines often receive multiple versions of the same event. Read `data/EventUpdates.csv` and keep only the latest update for each `EventID`.

Use `DictReader`, convert timestamp fields to `datetime` objects, and compare `UpdatedAt` values. Then report how many duplicate updates were found per event.

## Example Run
```console
python "src/22 Deduplicate Event Updates/solve.py"
```
