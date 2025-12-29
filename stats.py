def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_words():
    words = get_book_text("books/frankenstein.txt").split()
    count = 0
    for word in words:
        count += 1
    print(f"Found {count} total words")
    return count