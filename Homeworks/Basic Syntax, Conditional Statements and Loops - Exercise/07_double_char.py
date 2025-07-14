is_end = False

while not is_end:

    string = input()

    if string == "End":
        is_end = True
        break
    elif string == "SoftUni":
        continue

    for char in string:
        for n in range(2):
            print(f"{char}", end="")
    print('')
