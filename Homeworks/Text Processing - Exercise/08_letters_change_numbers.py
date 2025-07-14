string_list = input().split()
total_sum = 0

for string in string_list:
    number = int(string[1:len(string) - 1])
    first_letter = string[0]
    last_letter = string[-1]

    if first_letter.isupper():
        position = (ord(first_letter) - 64)
        total_sum += number / position
    elif first_letter.islower():
        position = (ord(first_letter) - 96)
        total_sum += number * position

    if last_letter.isupper():
        position = (ord(last_letter) - 64)
        total_sum -= position
    elif last_letter.islower():
        position = (ord(last_letter) - 96)
        total_sum += position



print(f"{total_sum:.2f}")