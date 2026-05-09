from collections import deque
def main():
    foods = deque(maxlen=5)
    foods.append("STA001")
    orders = ["DES003","STA002","ENT004","ENT001"]
    foods.extend(orders)
    foods.append("DES002")
    print(foods)
    return

if __name__ == "__main__":
    main()
