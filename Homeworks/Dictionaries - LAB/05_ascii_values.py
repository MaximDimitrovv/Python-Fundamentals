characters = input().split(", ")

print({letter: ord(letter) for letter in characters})
