def get_num_words(text):
    """
    Counts the number of words in the text.
    """
    word_count = len(text.split())
    print(f'{word_count} words found in the document')


def count_characters(text):
    """
    Counts the number of times each character appears in the text (lowercased).
    """
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts



