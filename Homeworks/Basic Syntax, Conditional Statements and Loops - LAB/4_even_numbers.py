n = int(input())

for num in range(1, n + 1):
    numbers = int(input())

    if not numbers % 2 == 0:
        print(f"{numbers} is odd!")
        break

    if num == n:
        print("All numbers are even.")