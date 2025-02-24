def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_characters(text):
    lower_text = text.lower()
    letter_dict = {}
    for character in lower_text:
        if character in letter_dict:
            letter_dict[character] += 1
        else:
            letter_dict[character] = 1
    return letter_dict

def get_sorted_list(dictionary):
    char_list = []
    for key, value in dictionary.items():
        char_list.append((key, value))
    sorted_list = sorted(char_list, key=lambda x: x[1], reverse=True)
    return sorted_list
