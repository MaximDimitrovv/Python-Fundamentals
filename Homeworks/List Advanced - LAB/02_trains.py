wagon_list = [0] * int(input())


is_end = False

while not is_end:

    command = input()

    if command == "End":
        is_end = True
        break

    if "add" in command:
        split_command = command.split(" ")
        people = int(split_command[1])
        wagon_list[-1] += people

    if "insert" in command:
        split_command = command.split(" ")
        wagon_index = int(split_command[1])
        people = int(split_command[2])
        wagon_list[wagon_index] += people

    if "leave" in command:
        split_command = command.split(" ")
        wagon_index = int(split_command[1])
        people = int(split_command[2])
        wagon_list[wagon_index] -= people

print(wagon_list)