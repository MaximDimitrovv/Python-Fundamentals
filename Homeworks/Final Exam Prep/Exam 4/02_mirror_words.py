import re

text_string = input()
pattern = r'#([a-zA-Z]{3,})##([a-zA-Z]{3,})#|@([a-zA-Z]{3,})@@([a-zA-Z]{3,})@'

valid_pairs_list = []
mirror_words = []

matches = re.finditer(pattern, text_string)

for match in matches:
    if match.group(1) and match.group(2):
        word_one = match.group(1)
        word_two = match.group(2)
    else:
        word_one = match.group(3)
        word_two = match.group(4)

    valid_pairs_list.append((word_one, word_two))

word_pairs_counter = len(valid_pairs_list)

for pair in valid_pairs_list:
    word_one = pair[0]
    word_two = pair[1][::-1]
    if word_one == word_two:
        valid = f"{word_one} <=> {pair[1]}"
        mirror_words.append(valid)

if word_pairs_counter > 0:
    print(f"{word_pairs_counter} word pairs found!")
else:
    print("No word pairs found!")

if len(mirror_words) > 0:
    print(f"The mirror words are:")
    print(", ".join(mirror_words))
else:
    print("No mirror words!")





