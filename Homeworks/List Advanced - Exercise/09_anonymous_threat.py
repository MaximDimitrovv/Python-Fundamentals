data = input().split()

while True:
    command = input()
    if command == "3:1":
        break

    parts = command.split()
    if parts[0] == "merge":
        start = int(parts[1])
        end = int(parts[2])

        if start < 0:
            start = 0
        if end >= len(data):
            end = len(data) - 1

        if start < end:
            merged = ''.join(data[start:end + 1])
            data[start:end + 1] = [merged]

    elif parts[0] == "divide":
        index = int(parts[1])
        partitions = int(parts[2])

        word = data[index]
        length = len(word)
        part_size = length // partitions
        extra = length % partitions

        new_parts = []
        last_index = 0

        for i in range(partitions):
            add = part_size + (1 if i == partitions - 1 else 0 and extra > 0)
            new_parts.append(word[last_index:last_index + part_size])
            last_index += part_size


        if last_index < length:
            new_parts[-1] += word[last_index:]

        data[index:index + 1] = new_parts

print(' '.join(data))

