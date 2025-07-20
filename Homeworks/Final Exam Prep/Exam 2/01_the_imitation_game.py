def move(line_list, num_of_letters):
    return line_list[num_of_letters:] + line_list[:num_of_letters]

def insert_value(line_list, index, value):
    for i in range(len(value) - 1, -1, -1):
        line_list.insert(index, value[i])
    return line_list

def change_all(line_list, sub, rep):
    string = "".join(line_list)
    string = string.replace(sub, rep)
    return list(string)

message = input()
message_list = list(message)

while "Decode" not in (line := input().split("|")):
    command = line[0]

    if command == "Move":
        num_of_letters = int(line[1])
        message_list = move(message_list, num_of_letters)

    elif command == "Insert":
        index = int(line[1])
        value = line[2]
        message_list = insert_value(message_list, index, value)

    elif command == "ChangeAll":
        substring = line[1]
        replacement = line[2]
        message_list = change_all(message_list, substring, replacement)

print(f"The decrypted message is: {''.join(message_list)}")
