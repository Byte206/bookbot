from stats import get_num_words
from stats import get_num_character
from stats import dict_sort
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    
    word_count = get_num_words(text)
    
    char_count = get_num_character(text)
    
    sorted_chars = dict_sort(char_count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char_info in sorted_chars:
        char = char_info["char"]
        num = char_info["num"]
        
        if char.isalpha():
            print(f"{char}: {num}")
    
    print("============= END ===============")

main()
