def palindrome_int(number):

    if number == number[::-1]:
        return True
    else:
        return False




string = input()
string_list = string.split(", ")

for index in string_list:
    print(palindrome_int(index))