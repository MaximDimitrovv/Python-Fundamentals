import re
string = input()

pattern_valid_emoji = r'::[A-Z][a-z]{2,}::|[*]{2}[A-Z][a-z]{2,}[*]{2}'
pattern_numbers = r'\d'

match_numbers = re.findall(pattern_numbers, string)

cool_threshold = 1
for number in match_numbers:
    cool_threshold *= int(number)
print(f"Cool threshold: {cool_threshold}")


match_emoji = re.findall(pattern_valid_emoji, string)
valid_emoji = []

print(f"{len(match_emoji)} emojis found in the text. The cool ones are:")

for emoji in match_emoji:
    total_number = 0
    for letter in emoji:
        if letter.isalpha():
            total_number += ord(letter)
    if total_number >= cool_threshold:
        print(emoji)
