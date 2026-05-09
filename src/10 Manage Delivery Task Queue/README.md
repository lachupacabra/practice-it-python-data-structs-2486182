# Practice It #10: Manage Delivery Task Queue

Implement queue helpers for delivery tasks.

`add_task()` should put priority tasks at the front and normal tasks at the back. `cancel_task()` should remove the first task matching an order ID while preserving the rest of the queue. `complete_next()` should return the next task or `None` when the queue is empty.

## Example Run
```console
python "src/10 Manage Delivery Task Queue/solve.py"
```
