number = int(input())
sum_of_char = 0

for _ in range(number):
    character = input()

    sum_of_char += ord(character)

print(f"The sum equals: {sum_of_char}")