import sys
from stats import get_num_words
from stats import get_character_counts
from stats import get_sorted_character_counts

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_word_count = get_num_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    character_counts = get_character_counts(book_text)
    sorted_character_counts = get_sorted_character_counts(character_counts)
    for dict in sorted_character_counts:
        print(f"{dict["character"]}: {dict["count"]}")
    print("============= END ===============")

main()