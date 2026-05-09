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
    inventory = Counter(starting)
    inventory.update(received)
    inventory.subtract(sold)
    inventory.subtract(spoiled)

    remaining_inventory = +inventory
    oversold_items = Counter(
        {product_id: abs(quantity) for product_id, quantity in inventory.items() if quantity < 0}
    )
    low_stock_items = Counter(
        {
            product_id: quantity
            for product_id, quantity in remaining_inventory.items()
            if quantity <= low_stock_threshold
        }
    )

    return {
        "remaining_inventory": remaining_inventory,
        "oversold_items": oversold_items,
        "low_stock_items": low_stock_items,
    }


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
