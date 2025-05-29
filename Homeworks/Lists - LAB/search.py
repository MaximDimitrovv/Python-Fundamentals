number = int(input())
word = input()
list_of_words = []

for _ in range(number):
    strings = input()
    list_of_words.append(strings)
print(list_of_words)

for no_word in list_of_words:
    if word not in no_word:
        list_of_words.remove(no_word)

print(list_of_words)

