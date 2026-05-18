from collections import Counter


def main():
    # TODO:
    # Use Counter to model inventory, subtract sold items, and add restocked items.
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    sales = {"STA001": 5, "SAL002": 3, "ENT004": 3}
    print(inventory)


if __name__ == "__main__":
    main()
