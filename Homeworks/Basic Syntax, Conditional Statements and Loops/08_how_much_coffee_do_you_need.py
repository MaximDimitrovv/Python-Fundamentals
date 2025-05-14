is_end = False
coffee = 0

while not is_end:

    command = input()

    if command == "END":
        is_end = True
        break

    if command == "dog" or command == 'cat' or command == 'coding' or command == 'movie':
        coffee += 1
    elif command == "DOG" or command == 'CAT' or command == 'CODING' or command == 'MOVIE':
        coffee += 2

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)