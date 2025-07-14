first_index = int(input())
second_index = int(input())
string = ''

for i in range(first_index, second_index + 1):
    string += chr(i) + " "

print(string)

