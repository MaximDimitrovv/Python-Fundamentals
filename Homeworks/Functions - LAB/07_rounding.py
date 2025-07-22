def rounding(string):
    string_list = string.split(" ")
    num_string = []

    for index in string_list:
        number = round(float(index))
        num_string.append(number)

    return num_string

string_of_numbers = input()

print(rounding(string_of_numbers))