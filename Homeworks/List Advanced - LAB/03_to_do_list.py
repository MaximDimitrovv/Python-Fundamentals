to_do_list = [0] * 10

is_end = False

while not is_end:

    command = input()

    if command == "End":
        is_end = True
        break

    split_command = command.split("-")
    priority_index = int(split_command[0]) - 1
    to_do = split_command[1]
    to_do_list.pop(priority_index)
    to_do_list.insert(priority_index, to_do)

print([zero for zero in to_do_list if zero != 0])