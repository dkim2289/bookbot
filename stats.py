def word_counter(text):
	words = text.split()
	return len(words)

def get_chars_dict(text: str) -> dict[str, int]:
    dict = {}
    for ea_char in text:
        lowered = ea_char.lower()
        if lowered in dict:
            dict[lowered] += 1
        else:
            dict[lowered] = 1
    return dict

def char_counter(text):
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

def sort_by_nums(dic):
	sorted_list = []
	for item in dic:
		if item.isalpha() == False:
			continue
		else:
			sorted_list.append({"char": item, "num": dic[item]})
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list
