n = int(input())

for num in range(1, n + 1):
    print("*" * num)

for num in range(n - 1, 0, -1):
    print("*" * num)