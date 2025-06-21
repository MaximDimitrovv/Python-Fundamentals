message = input()
words = message.split()
decoded_words = []

for word in words:
    number = ''
    for char in word:
        if char.isdigit():
            number += char
        else:
            break

    first_letter = chr(int(number))

    rest = word[len(number):]

    letters = list(rest)
    if len(letters) >= 2:
        letters[0], letters[-1] = letters[-1], letters[0]

    decoded_word = first_letter + ''.join(letters)
    decoded_words.append(decoded_word)

decoded_message = ' '.join(decoded_words)
print(decoded_message)