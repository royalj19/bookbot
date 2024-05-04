def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count_words(text):
    words = text.split()
    return len(words)

def get_count_letters(text):
    lowercase = text.lower()
    letter_dict = {}
    for char in lowercase:
        if  char.isalpha():
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1
    letter_list = [{"letter": letter, "counted": counted} for letter, counted in letter_dict.items()]
    return letter_list

def sort_on(item):
    return item["counted"]



def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_count_words(text)
    letters = get_count_letters(text)
    letters.sort(key=sort_on, reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()
    for item in letters:
        print(f"The '{item['letter']}' character was found {item['counted']} times")
    print("--- End report ---")

    

main()
