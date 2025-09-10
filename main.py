import sys
from stats import get_num_words, get_characters_dict, get_list

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def print_report(path_book, text):
    num_words = get_num_words(text)
    chars_dict = get_characters_dict(text)
    sorted_list = get_list(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")
    
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    path_book = sys.argv[1]    
    text = get_book_text(path_book)
    print_report(path_book, text)

main()