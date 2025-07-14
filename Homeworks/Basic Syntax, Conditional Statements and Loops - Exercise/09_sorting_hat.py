is_welcome = False

while not is_welcome:

    name = input()

    if name == 'Welcome!':
        print("Welcome to Hogwarts.")
        is_welcome = True
        break

    if name == 'Voldemort':
        print("You must not speak of that name!")
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")