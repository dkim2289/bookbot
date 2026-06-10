def word_counter(text: str) -> int:
	words = text.split()
	return len(words)

def get_chars_dict(text: str) -> dict[str, int]:
	text = text.lower()
	char_dic = {}
	for char in text:
		if char in char_dic:
			char_dic[char] += 1
		else:
			char_dic[char] = 1
	return char_dic

def sort_on(char_count: tuple[str, int]) -> int:
	return char_count[1]

def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str,int]]:
	chars_list: list[tuple[str,int]] = []
	for char in chars_dict:
		count = chars_dict[char]
		chars_list.append((char, count))
	return sorted(chars_list, reverse=True, key=sort_on)
