phonebook = {}

while True:
    info = input()

    if info.isdigit():
        num = int(info)

        for _ in range(num):
            name = input()
            if name in phonebook:
                print(f"{name} -> {phonebook[name]}")
            else:
                print(f"Contact {name} does not exist.")
        break

    split = info.split("-")
    name = split[0]
    phone = split[1]

    phonebook[name] = phone


