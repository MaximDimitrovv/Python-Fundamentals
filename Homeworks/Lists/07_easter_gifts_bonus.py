gifts_string = input()
list_of_gifts = gifts_string.split(" ")

no_more_money = False

while not no_more_money:

    command = input()

    if command == "No Money":
        no_more_money = True
        break

    list_of_command = command.split(" ")

    if list_of_command[0] == "OutOfStock":
        for i in range(len(list_of_gifts)):
            if list_of_gifts[i] == list_of_command[1]:
                list_of_gifts[i] = "None"

    elif list_of_command[0] == "Required":
        index = int(list_of_command[2])
        if 0 <= index < len(list_of_gifts):
            list_of_gifts[index] = list_of_command[1]

    elif list_of_command[0] == "JustInCase":
        list_of_gifts[-1] = list_of_command[1]

final_list = []

for items in list_of_gifts:
    if items != "None":
        final_list.append(items)

print(" ".join(final_list))
