from collections import deque


def check_palindrome(word):
    dq_word = deque(word.lower())
    while len(dq_word) > 1:
        if dq_word.pop() != dq_word.popleft():
            return False
    return True


def main():
    items = ["Tacocat", "choice"]
    for word in items:
        print(f"{word} is palindrome :{check_palindrome(word)}")


if __name__ == "__main__":
    main()
