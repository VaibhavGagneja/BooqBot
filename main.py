from stats import num_words, count_characters
import sys
def get_book_text(pathfile):
    return open(pathfile,'r',encoding='utf-8').read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = 'books/frankenstein.txt'
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    book_text = get_book_text(filepath)
    words = num_words(book_text)
    if words:
        print("----------- Word Count ----------")
        print(f"Found {words} total words")
    char_stats = count_characters(book_text)
    print("--------- Character Count -------")
    for char, count in list(char_stats.items()):
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
    