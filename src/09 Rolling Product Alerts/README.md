# Practice It #9: Rolling Product Alerts

Implement `rolling_product_alerts()` to detect product surges in a rolling window of order events.

Use a fixed-size `deque` for recent events and a `Counter` for product counts. When a product reaches the surge threshold, append an alert dictionary with the triggering event, product count, and recent event IDs.

## Example Run
```console
python "src/09 Rolling Product Alerts/solve.py"
```
