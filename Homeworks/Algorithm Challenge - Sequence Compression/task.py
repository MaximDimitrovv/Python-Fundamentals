numbers_to_add = int(input())
sequence = []

for _ in range(numbers_to_add):
    numbers = int(input())
    sequence.append(numbers)

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
