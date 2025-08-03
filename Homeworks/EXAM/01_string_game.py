

string = input()


while (command := input()) != "Done":
    split_command = command.split()
    action = split_command[0]

    match action:
        case "Change":
            char = split_command[1]
            replacement = split_command[2]

            string = string.replace(char, replacement)
            print(string)
        case "Includes":
            substring = split_command[1]

            if substring in string:
                print(True)
            else:
                print(False)
        case "End":
            substring = split_command[1]

            if string.endswith(substring):
                print(True)
            else:
                print(False)
        case "Uppercase":

            string = string.upper()
            print(string)
        case "FindIndex":
            char = split_command[1]

            for i in range(len(string)):
                if string[i] == char:
                    print(i)
                    break
        case "Cut":
            start_index = int(split_command[1])
            count = int(split_command[2])

            string = string[start_index:start_index+count]
            print(string)