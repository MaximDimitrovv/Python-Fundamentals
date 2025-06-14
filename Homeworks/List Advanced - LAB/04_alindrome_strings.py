random_words = input()
palindrome = input()

words_list = random_words.split(" ")
palindrome_list = []

for word in words_list:
    new_word = ''
    for i in range(len(word) - 1, -1, -1):
        new_word += word[i]

    if new_word == word:
        palindrome_list.append(new_word)

print(palindrome_list)

counter = 0
for palindrome_word in palindrome_list:
    if palindrome_word == palindrome:
        counter += 1

print(f"Found palindrome {counter} times")
