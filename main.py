from stats import get_num_words, get_char_counts_sorted
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at ${book_path}")

    
    text = get_book_text(book_path)

    print("----------- Word Count ----------")
    get_num_words(text)

    print("--------- Character Count -------")
    sorted_characters = get_char_counts_sorted(text)

    for entry in sorted_characters:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

main()

    
