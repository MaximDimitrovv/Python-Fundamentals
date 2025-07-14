string_of_numbers = input()
num_of_beggars = int(input())

list_of_numbers = string_of_numbers.split(", ")
final_list = [0] * num_of_beggars


for i in range(len(list_of_numbers)):
    index = i % num_of_beggars
    final_list[index] += int(list_of_numbers[i])

print(final_list)
