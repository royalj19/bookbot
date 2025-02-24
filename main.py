import sys
from stats import *

def main():
    if len(sys.argv) != 2:
        print("usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    text = get_book_text(path)
    word_count = get_num_words(text)
    character_dict = get_num_characters(text)
    sorted_list = get_sorted_list(character_dict)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for character, count in sorted_list:
        if character.isalpha():
            print(f"{character}: {count}")

    print("============= END ===============")

main()