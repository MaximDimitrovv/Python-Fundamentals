electrons = int(input())

shells = []
n = 1

while electrons > 0:
    capacity = 2 * n ** 2

    if electrons >= capacity:
        shells.append(capacity)
        electrons -= capacity
    else:
        shells.append(electrons)
        electrons = 0
    n += 1

print(shells)