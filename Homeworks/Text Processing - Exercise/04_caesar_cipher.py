string = input()
new_string = ''

for letter in string:

    ascii_number = ord(letter)
    ascii_number += 3
    new_string += chr(ascii_number)

print(new_string)