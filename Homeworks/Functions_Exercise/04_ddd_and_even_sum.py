def odd_sum(given_number):
    number_to_string = str(given_number)
    odd = 0
    for i in range(len(number_to_string)):
        number_index = int(number_to_string[i])
        if number_index % 2 != 0:
            odd += number_index

    return odd

def even_sum(given_number):
    number_to_string = str(given_number)
    even = 0
    for i in range(len(number_to_string)):
        number_index = int(number_to_string[i])
        if number_index % 2 == 0:
            even += number_index

    return even

number = int(input())

print(f"Odd sum = {odd_sum(number)}, Even sum = {even_sum(number)}")