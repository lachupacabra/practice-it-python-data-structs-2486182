# Practice It #14: Validate Delivery Status Transitions

Implement delivery event helpers using `namedtuple` records.

`parse_event()` should convert raw tuples into `DeliveryEvent` values with `datetime` timestamps. `find_invalid_transitions()` should report statuses that move backward or occur after a terminal delivered/canceled status. `update_status()` should return an updated copy of an immutable event.

## Example Run
```console
python "src/14 Validate Delivery Status Transitions/solve.py"
```
