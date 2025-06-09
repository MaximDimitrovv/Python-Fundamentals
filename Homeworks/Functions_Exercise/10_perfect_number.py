def perfect_number(num):

    number = 0

    for divisor in range(1, num + 1):

        if number == num:
            break

        if num % divisor == 0:
            number += divisor

    if number == num:
        return True
    else:
        return False


integer = int(input())

if perfect_number(integer):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")