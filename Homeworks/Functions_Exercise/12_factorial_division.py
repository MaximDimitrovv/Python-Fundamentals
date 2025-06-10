def factorial_division(first_num, second_num):
    first_multiply = 1

    for num in range(2, first_num + 1):
        first_multiply *= num

    second_multiply = 1
    for num in range(2, second_num + 1):
        second_multiply *= num

    return first_multiply / second_multiply


first_number = int(input())
second_number = int(input())
print(f"{factorial_division(first_number, second_number):.2f}")
