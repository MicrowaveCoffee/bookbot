from stats import get_num_words, get_char_counts_sorted

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)

    print("----------- Word Count ----------")
    get_num_words(text)

    print("--------- Character Count -------")
    sorted_characters = get_char_counts_sorted(text)

    for entry in sorted_characters:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

main()

    
