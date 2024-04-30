def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

main()
