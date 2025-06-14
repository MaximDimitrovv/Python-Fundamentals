string = input()
vowels = ['a', 'o', 'u', 'e', 'i']

no_vowels_list = [letter for letter in string if letter.lower() not in vowels]

print("".join(no_vowels_list))
