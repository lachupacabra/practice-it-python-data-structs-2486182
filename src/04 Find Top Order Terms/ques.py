import string
from collections import Counter
from pprint import pprint


ORDER_NOTES = [
    "Organic bananas added after customer requested organic produce.",
    "Refunded dairy-free yogurt; customer accepted coconut yogurt instead.",
    "Produce bag included bananas, apples, apples, and fresh basil.",
    "Customer asked for low-sodium soup and organic broth.",
    "Bananas were out of stock, replaced with organic plantains.",
    "Fresh produce and dairy-free snacks should be packed together.",
]

STOP_WORDS = {
    "a",
    "after",
    "and",
    "be",
    "for",
    "of",
    "out",
    "should",
    "the",
    "with",
}


def normalize_words(text):
    # TODO:
    # 1. Lowercase the text.
    # 2. Replace punctuation with spaces.
    # 3. Split the text into words.
    return []


def get_top_terms(notes, stop_words, top_n=5):
    # TODO:
    # Use Counter to count normalized words across every note.
    # Skip words in stop_words.
    # Return the top_n most common words as a list of (word, count) tuples.
    return []


def main():
    pprint(get_top_terms(ORDER_NOTES, STOP_WORDS, top_n=5))
    return


if __name__ == "__main__":
    main()
