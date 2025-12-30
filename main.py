from stats import get_book_text
from stats import num_words
from stats import character_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words()
    character_count()

main()