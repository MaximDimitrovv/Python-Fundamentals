number_list = input().split(", ")
even_list = []


for i in range(len(number_list)):
    num = int(number_list[i])

    if num % 2 == 0:
        even_list.append(i)

print(even_list)