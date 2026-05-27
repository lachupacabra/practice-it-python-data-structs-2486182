# Practice It #24: Load Incremental Changes

Incremental pipelines usually load only rows newer than the last successful watermark.

Read `data/CustomerChangeLog.csv`, filter records where `UpdatedAt` is later than a supplied watermark, and compute the next watermark after the load finishes.

## Example Run
```console
python "src/24 Load Incremental Changes/solve.py"
```
