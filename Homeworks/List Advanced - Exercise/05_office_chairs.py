number_of_rooms = int(input())
rooms_info = []
total_chairs = 0
total_visitors = 0

for room in range(1, number_of_rooms + 1):
    office_info = input().split(" ")
    chairs = len(office_info[0])
    visitors = int(office_info[1])
    rooms_info += [[chairs, visitors]]

    total_chairs += chairs
    total_visitors += visitors



if total_chairs >= total_visitors:
    chairs_left = total_chairs - total_visitors
    print(f"Game On, {chairs_left} free chairs left")
else:
    for i in range(len(rooms_info)):
        room_number = i + 1
        chairs = rooms_info[i][0]
        visitors = rooms_info[i][1]
        if chairs < visitors:
            chairs_needed = visitors - chairs
            print(f"{chairs_needed} more chairs needed in room {room_number}")








