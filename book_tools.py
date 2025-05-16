def get_book_text(filepath):
    """returns entire text of a book as a string"""
    with open(filepath) as file:
        content = file.read()
    return content

def count_words(text):
    """counts the number of words in text"""
    return len(text.split())

def find_chapters(text):
    """Finds where chapters begin in the text. return a list of (chapter_number, starting_position) tuples."""
    import re

    chapter_pattern = re.compile(r'chapter\s+([IVDXCML]+|d+)', re.IGNORECASE)
