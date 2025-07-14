string = input()
new_string = ""
last_letter = ''

for letter in string:
    if letter == last_letter:
        continue

    new_string += letter
    last_letter = letter

print(new_string)