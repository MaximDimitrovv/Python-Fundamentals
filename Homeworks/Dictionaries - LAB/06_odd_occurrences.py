line = input().lower().split(" ")

words = {}

for i in range(len(line)):

    if line[i] in words:
        words[line[i]] += 1
        continue
    words[line[i]] = 1

for key, value in words.items():
    if not value % 2 == 0:
        print(key, end=" ")