def get_num_words(text):
    return len(text.split())

def get_num_character(text):
    text = text.lower()
    counter = {}
    for character in text:
        if character in counter:
            counter[character] += 1
        else:
            counter[character] = 1
    return counter

def sort_on(dict_item):
    return dict_item["num"]

def dict_sort(dict):
    char_list = []
    for char, count in dict.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(key=sort_on, reverse=True)
    return char_list
