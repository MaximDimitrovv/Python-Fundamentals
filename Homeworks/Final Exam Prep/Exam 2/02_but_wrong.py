data = input()

info = []
total_calories = 0

i = 0
while i < len(data):
    if data[i] == "#" or data[i] == "|":
        delimiter = data[i]
        opposite_delimiter = ''

        if delimiter == "#":
            opposite_delimiter = "|"
        elif delimiter == '|':
            opposite_delimiter = "#"

        i += 1
        new_data = []
        delimiter_counter = 0

        for j in range(i, len(data)):
            if data[j] == delimiter:
                delimiter_counter += 1
                if delimiter_counter == 1:
                    name = data[i:j]
                    if not name.strip() or not all(char.isspace() or char.isalpha() for char in name):
                        i = j
                        break
                elif delimiter_counter == 2:
                    date = data[i:j]

                    slash_counter = 0
                    for char in date:
                        if char == '/':
                            slash_counter += 1

                    if slash_counter == 2:
                        split_date = date.split("/")
                        if not all(len(integer) == 2 and integer.isdigit() for integer in split_date):
                            i = j
                            break
                    else:
                        i = j
                        break
                elif delimiter_counter == 3:
                    calories = data[i:j]
                    if calories.isdigit():
                        if not 0 <= int(calories):
                            i = j
                            break
                    else:
                        i = j
                        break
                new_data.append(data[i:j])
                i = j + 1
                if len(new_data) == 3:
                    break
            elif data[j] == opposite_delimiter:
                i = j
                break
        if len(new_data) == 3:
            calories = int(new_data[2])
            total_calories += calories
            new_data[2] = calories
            info.append(new_data)
    else:
        i += 1
days_left = total_calories // 2000
print(f"You have food to last you for: {days_left} days!")
for item in info:
    name = item[0]
    date = item[1]
    calories = item[2]
    print(f"Item: {name}, Best before: {date}, Nutrition: {calories}")
