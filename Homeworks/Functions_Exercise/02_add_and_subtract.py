
def add_and_subtract(first_num, second_num, third_num):

    def sum_numbers():
        return first_num + second_num

    def subtract(result):
        return result - third_num

    sum_result = sum_numbers()
    return subtract(sum_result)


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(add_and_subtract(num_1, num_2, num_3))