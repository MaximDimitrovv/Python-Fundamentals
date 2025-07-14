string_1, string_2 = input().split()
result = 0


if len(string_1) >= len(string_2):
    for i in range(len(string_1)):
        if len(string_2) < i + 1:
            result += ord(string_1[i])
        else:
            result += ord(string_1[i]) * ord(string_2[i])
else:
    for i in range(len(string_2)):
        if len(string_1) < i + 1:
            result += ord(string_2[i])
        else:
            result += ord(string_2[i]) * ord(string_1[i])

print(result)