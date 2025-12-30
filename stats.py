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

def character_count():
    character_dict = {}
    words = list(get_book_text("books/frankenstein.txt").split())

    for word in words:
        characters = list(word)
        for character in characters:
            if character.lower() in character_dict:
                character_dict[character.lower()] += 1
            else:
                character_dict[character.lower()] = 1

    return character_dict
    