string = input().split(" ")

def merge(whole_command, string_list):
    split = whole_command.split(" ")
    start_index = int(split[1])
    end_index = int(split[2]) + 1

    string_list[start_index:end_index] = ["".join(string_list[start_index:end_index])]

    return string_list


def divide(whole_command, string_list):
    split = whole_command.split(" ")
    index = int(split[1])
    parts = int(split[2])

    split_word = string_list[index]
    letters_list = []
    for i in range(len(split_word)):
        if len(split_word) % 2 == 0:


    return letters_list

print(divide("divide 0 2", string))
# while True:
#     command = input()
#
#     if command == "3:1":
#         break
#
#     if "merge" in command:

