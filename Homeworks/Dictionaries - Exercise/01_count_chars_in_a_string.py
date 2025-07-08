line = input().split(" ")
string = "".join(line)

occur = {}

for letter in string:

    if letter not in occur:
        occur[letter] = 1
    else:
        occur[letter] += 1

for key in occur:
    print(f"{key} -> {occur[key]}")
