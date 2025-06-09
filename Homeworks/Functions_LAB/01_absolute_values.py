def absolute_values(string_input):
    string_list = string_input.split(" ")
    number_list= []


    for index in string_list:
        numbers = float(index)
        number_list.append(abs(numbers))

    return number_list

string = input()
print(absolute_values(string))