number = int(input())

for first_number in range(number):
    for second_number in range(number):
        for third_number in range(number):
            first = chr(97 + first_number)
            second = chr(97 + second_number)
            third = chr(97 + third_number)

            print(f"{first}{second}{third}")