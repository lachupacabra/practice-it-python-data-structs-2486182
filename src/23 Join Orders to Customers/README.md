# Practice It #23: Join Orders to Customers

Data engineering interviews often ask you to join two datasets without using a database.

Read `data/CustomerAccounts.csv` and `data/OrdersForJoin.csv`, join orders to customer accounts by `CustomerID`, flag orders that do not have a matching customer, and calculate completed revenue by customer segment.

## Example Run
```console
python "src/23 Join Orders to Customers/solve.py"
```
