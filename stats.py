def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars

def sort_on(items):
    return items["num"]

def get_list(char_dict):
    list_dict = []
    for k in char_dict:
        if k.isalpha():
            list_dict.append({"char": k, "num": char_dict[k]})

    list_dict.sort(reverse=True, key=sort_on)
    return list_dict