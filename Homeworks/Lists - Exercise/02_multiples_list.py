factor = int(input())
count = int(input())

new_list = []
new_number = 0

for num in range(count):
    new_number += factor
    new_list.append(new_number)

print(new_list)

