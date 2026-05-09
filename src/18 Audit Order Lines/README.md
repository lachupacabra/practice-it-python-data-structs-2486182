# Practice It #18: Audit Order Lines

Implement `audit_order_lines()` to separate valid order lines from anomalous records.

Use `defaultdict(list)` to group bad records by anomaly reason and `defaultdict(int)` to aggregate valid quantities by product. Detect duplicate item IDs, non-positive quantities, unknown product prefixes, and unusually large quantities greater than 10.

## Example Run
```console
python "src/18 Audit Order Lines/solve.py"
```
