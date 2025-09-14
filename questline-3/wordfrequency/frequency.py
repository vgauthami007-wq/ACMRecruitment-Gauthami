from collections import Counter
import re

def word_frequency(text: str):
    """
    Count frequency of each unique word in the given text.
    Returns a dictionary sorted by frequency (highest -> lowest).
    """
    # Normalize text: lowercase, remove punctuation
    words = re.findall(r"\b\w+\b", text.lower())
    counter = Counter(words)
    return dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))

if __name__ == "__main__":
    # Read input from file
    with open("input.txt", "r") as f:
        text = f.read()

    # Process frequency
    frequencies = word_frequency(text)

    # Write results to file
    with open("output.txt", "w") as f:
        for word, count in frequencies.items():
            f.write(f"{word} -> {count}\n")

    print("Word frequencies written to output.txt")
