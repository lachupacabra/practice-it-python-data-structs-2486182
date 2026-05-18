import string
from collections import Counter
from pprint import pprint
import re

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

    # text = text.lower()
    # text = text.translate(str.maketrans("","",string.punctuation))
    # print(text)
    words = re.findall(r'[a-z]+', text.lower())
    return words


def get_top_terms(notes, stop_words, top_n=5):
    # TODO:
    # Use Counter to count normalized words across every note.
    # Skip words in stop_words.
    # Return the top_n most common words as a list of (word, count) tuples.
    counts=Counter()
    for note in notes:
        words = normalize_words(note)
        kept_words = [word for word in words if word not in stop_words]
        # print(kept_words)
        counts.update(kept_words)
    return counts.most_common(top_n)


def main():
    pprint(get_top_terms(ORDER_NOTES, STOP_WORDS, top_n=5))
    return


if __name__ == "__main__":
    main()
