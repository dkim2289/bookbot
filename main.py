import sys
from stats import word_counter, char_counter, sort_by_nums


def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	book_text = get_book_text(book_path)
	num_words = word_counter(book_text)
	# next line needs to be changed as to get chars dictionary, instead of char count
	char_count = char_counter(book_text)
	# next line needs to sort the chars_dict instead of char_count
	sorted_list = sort_by_nums(char_count)
    print_report(book_path, num_words, chars_sorted_list)

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def print_report(
    book_path: str,
    num_words: int,
    chars_sorted_list: list[tuple[str, int]]
) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in chars_sorted_list:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

    print("============= END ===============")

main()
