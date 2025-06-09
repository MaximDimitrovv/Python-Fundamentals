def even_numbers(x):
    number = int(x)
    if number % 2 == 0:
        return True

string = input()
string_list = string.split(" ")

filtered = filter(even_numbers, string_list)

print(list(map(int, filtered)))