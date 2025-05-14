divisor = int(input())
boundary = int(input())

for num in range(boundary + 1, 0, -1):
    if num % divisor == 0 and boundary >= num > 0:
        print(num)
        break