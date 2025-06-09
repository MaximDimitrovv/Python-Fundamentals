def sort(num_string):

    string_list = num_string.split(" ")
    number_list = []

    for index in string_list:
        number_list.append(int(index))

    return sorted(number_list)


string = input()

print(sort(string))