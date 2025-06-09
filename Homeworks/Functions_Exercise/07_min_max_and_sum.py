def min_sum(number_list):
    return min(number_list)


def max_sum(number_list):
    return max(number_list)

def total_sum(number_list):
    return sum(number_list)


string = input()

string_list = string.split(" ")
num_list = []

for index in string_list:
    num_list.append(int(index))

print(f"The minimum number is {min_sum(num_list)}")
print(f"The maximum number is {max_sum(num_list)}")
print(f"The sum number is: {total_sum(num_list)}")