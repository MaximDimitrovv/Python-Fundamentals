materials = {
    "key_fragments":
        {
            "shards":
                {
                    "name": "Shadowmourne",
                    "quantity": 0
                },
            "fragments":
                {
                    "name": "Valanyr",
                    "quantity": 0
                },
            "motes":
                {
                    "name": "Dragonwrath",
                    "quantity": 0
                },
        },
    "junk":
        {}
}


while True:
    line = input().split(" ")
    is_obtained = False

    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1].lower()

        if material not in materials["key_fragments"]:
            if material not in materials["junk"]:
                materials["junk"][material] = quantity
            else:
                materials["junk"][material] += quantity
        else:
            materials["key_fragments"][material]["quantity"] += quantity

        for key in materials["key_fragments"]:
            if materials["key_fragments"][key]["quantity"] >= 250:
                materials["key_fragments"][key]["quantity"] -= 250
                name = materials["key_fragments"][key]["name"]
                print(f"{name} obtained!")
                is_obtained = True
                break
        if is_obtained:
            break

    if is_obtained:
        for key, value in materials.items():
            for k, v in value.items():
                if key == "key_fragments":
                    print(f"{k}: {v['quantity']}")
                else:
                    print(f"{k}: {v}")
        break