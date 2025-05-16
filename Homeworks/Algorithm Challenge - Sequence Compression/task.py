sequence = [1, 1, 1, 2, 2, 3, 1, 1, 1, 2, 3, 3, 5, 5]
#
first_number = sequence[0]
counter = 0
index = 0

compressed = []

for number in sequence:
    if number  != first_number:
        compressed.append((first_number, counter))
        counter = 1
        first_number = number
    else:
        counter += 1
else:
    compressed.append((first_number, counter))

print(compressed)
