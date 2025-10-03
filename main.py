import sys
from stats import word_counter, char_counter, sort_by_nums

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	book_text = get_book_text(book_path)
	num_words = word_counter(book_text)
	char_count = char_counter(book_text)
	sorted_list = sort_by_nums(char_count)
	
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in sorted_list:
		print(f"{item["char"]}: {item["num"]}\n")
	print("============= END ===============")

main()
