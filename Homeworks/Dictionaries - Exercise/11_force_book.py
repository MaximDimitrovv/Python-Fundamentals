force_book = {}


while (line := input()) != "Lumpawaroo":

    if "|" in line:
        force_side, force_user = line.split(" | ")

        if force_side not in force_book:
            force_book[force_side] = []

        is_on_any_side = False
        for side in force_book:
            if force_user in force_book[side]:
                is_on_any_side = True

        if not is_on_any_side:
            force_book[force_side].append(force_user)

    elif "->" in line:
        force_user, force_side = line.split(" -> ")

        if force_side not in force_book:
            force_book[force_side] = []

        for side in force_book:
            if force_user in force_book[side]:
                force_book[side].remove(force_user)
                break

        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")


for side, key in force_book.items():
    if len(force_book[side]) > 0:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        for name in key:
            print(f"! {name}")