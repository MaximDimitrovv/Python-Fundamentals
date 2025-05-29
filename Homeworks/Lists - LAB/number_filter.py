number = int(input())

list_integers = []
for _ in range(number):
    integers = int(input())
    list_integers.append(integers)

command = input()
new_list = []


for n in list_integers:
    if command == 'odd':
        if not n % 2 == 0:
            new_list.append(n)
    elif command == 'even':
        if n % 2 == 0:
            new_list.append(n)
    elif command == 'negative':
        if not n >= 0:
            new_list.append(n)
    elif command == 'positive':
        if n >= 0:
            new_list.append(n)

print(new_list)
