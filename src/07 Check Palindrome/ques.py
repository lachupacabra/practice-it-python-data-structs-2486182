from collections import deque


def check_palindrome(word):
    # TODO:
    # Use a deque to compare characters from both ends of the word.
    return False


def main():
    items = ["Tacocat", "choice"]
    for word in items:
        print(f"{word} is palindrome :{check_palindrome(word)}")


if __name__ == "__main__":
    main()
