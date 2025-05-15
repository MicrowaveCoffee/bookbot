from stats import get_num_words, count_characters

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    result = get_book_text('books/frankenstein.txt')

    # Word count
    get_num_words(result)

    # Character count
    char_counts = count_characters(result)
    print("Character Counts:")
    print(char_counts)

main()


    
