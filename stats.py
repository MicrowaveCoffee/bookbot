def get_num_words(text):
    """
    Counts the number of words in the text.
    """
    word_count = len(text.split())
    print(f'Found {word_count} total words')


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

def get_char_counts_sorted(text):
    char_counts = {}

    for char in text.lower():
        if char.isalpha():  # only count alphabetical characters
            if char not in char_counts:
                char_counts[char] = 0
            char_counts[char] += 1

    # Convert to list of dictionaries
    char_list = [{"char": k, "num": v} for k, v in char_counts.items()]

    # Sort by 'num' from greatest to least
    char_list.sort(key=lambda x: x["num"], reverse=True)

    return char_list
    
    




