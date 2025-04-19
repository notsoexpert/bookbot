def get_num_words(text):
    return len(text.split())

def get_character_counts(text):
    dict = {}

    for char in text:
        char = char.lower()
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def sort_on(dict):
    return dict["count"]

def get_sorted_character_counts(character_dict):
    dict_list = []
    count = 0
    for k, v in character_dict.items():
        if not k.isalpha():
            continue

        dict_list.append({
            "character": k, "count": v
        })
        count += 1
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list