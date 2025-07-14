string = input()
shuffle = int(input())

list_of_string = string.split(" ")
half = len(list_of_string) // 2

while shuffle > 0:
    first_half = []
    second_half = []

    for i in range (half):
        first_half.append(list_of_string[i])

    for j in range(half, len(list_of_string)):
        second_half.append(list_of_string[j])

    for card in range(len(list_of_string)):
        if card % 2 == 0:
            list_of_string[card] = (first_half[card // 2])
        else:
            list_of_string[card] = (second_half[card // 2])
    shuffle -= 1

print(list_of_string)