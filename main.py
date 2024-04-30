def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_words(something):
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count
    

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    word_count = count_words(book_path)
    print(word_count)

main()
