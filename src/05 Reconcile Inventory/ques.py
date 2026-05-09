from collections import Counter
from pprint import pprint


STARTING_INVENTORY = Counter(
    BANANA=24,
    APPLE=18,
    YOGURT=12,
    SOUP=9,
    BASIL=6,
    PLANTAIN=0,
)

RECEIVED_STOCK = Counter(BANANA=10, YOGURT=8, PLANTAIN=12, BASIL=4)
SALES = Counter(BANANA=31, APPLE=7, YOGURT=16, SOUP=11, BASIL=8, PLANTAIN=4)
SPOILAGE = Counter(BANANA=2, APPLE=1, BASIL=1)


def reconcile_inventory(starting, received, sold, spoiled, low_stock_threshold=5):
    # TODO:
    # Use Counter operations to apply received stock, sales, and spoilage.
    # Return a dictionary with:
    #   remaining_inventory: only products with positive inventory
    #   oversold_items: products whose final inventory went below zero
    #   low_stock_items: positive inventory at or below low_stock_threshold
    return {}


def main():
    pprint(
        reconcile_inventory(
            STARTING_INVENTORY,
            RECEIVED_STOCK,
            SALES,
            SPOILAGE,
            low_stock_threshold=5,
        )
    )
    return


if __name__ == "__main__":
    main()
