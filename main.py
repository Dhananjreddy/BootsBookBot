import sys
from stats import get_num_words, check_letters, sorter

def main():
    if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
    
    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)
    letters = check_letters(book)
    arranged = sorter(letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter, count in arranged:
        print(f"{letter}: {count}")
    print("============= END ===============")



def get_book_text(input):
    with open(input) as file:
      text = file.read()
      return text

if __name__ == "__main__":
    main()

