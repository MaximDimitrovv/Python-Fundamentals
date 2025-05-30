import sys

string = input()
num_to_remove = int(input())

list_of_numbers = []

for num in string.split(" "):
    list_of_numbers.append(int(num))


for _ in range(num_to_remove):
    list_of_numbers.remove(min(list_of_numbers))

list_of_string = []
for char in list_of_numbers:
    list_of_string.append(str(char))

print(", ".join(list_of_string))