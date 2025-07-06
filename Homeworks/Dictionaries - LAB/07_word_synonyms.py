n = int(input())

all_words = {}

for _ in range(n):
    word = input()
    synonym = input()

    if word in all_words:
        all_words[word].append(synonym)
        continue
    all_words[word] = [synonym]


for key, value in all_words.items():
    print(f"{key} - {', '.join(value)}")

