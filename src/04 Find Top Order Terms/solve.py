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
    translator = str.maketrans({mark: " " for mark in string.punctuation})
    cleaned_text = text.lower().translate(translator)
    return cleaned_text.split()


def get_top_terms(notes, stop_words, top_n=5):
    counts = Counter()
    for note in notes:
        words = normalize_words(note)
        counts.update(word for word in words if word not in stop_words)
    return counts.most_common(top_n)


def main():
    pprint(get_top_terms(ORDER_NOTES, STOP_WORDS, top_n=5))
    return


if __name__ == "__main__":
    main()
