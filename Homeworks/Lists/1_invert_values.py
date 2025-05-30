string = input()

list_of_numbers = string.split(" ")

for i in range(len(list_of_numbers)):
    num = int(list_of_numbers[i])
    new_number = num - (num * 2)
    list_of_numbers[i] = new_number

print(list_of_numbers)

