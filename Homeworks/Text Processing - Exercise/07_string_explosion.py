string = input()
new_string = ""
explosion_strength = 0


for i in range(len(string)):

    if explosion_strength > 0 and string[i] != ">":
        explosion_strength -= 1
    elif string[i] == ">":
        new_string += string[i]
        explosion_strength += int(string[i + 1])
    else:
        new_string += string[i]

print(new_string)