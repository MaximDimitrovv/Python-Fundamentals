n = int(input())

parking_lot = {}

for _ in range(n):
    info = input().split(" ")

    command = info[0]
    name = info[1]

    if command == "register":
        plate_number = info[2]
        if name not in parking_lot:
            parking_lot[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            existing_plate = parking_lot[name]
            print(f"ERROR: already registered with plate number {existing_plate}")
    elif command == "unregister":
        if name not in parking_lot:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del parking_lot[name]

for key, value in parking_lot.items():
    print(f"{key} => {value}")
