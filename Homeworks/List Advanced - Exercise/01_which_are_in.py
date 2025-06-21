list_one = input().split(", ")
list_two = input().split(", ")

final_list = []

for word_one in list_one:
    for word_two in list_two:
        if word_one in word_two and word_one not in final_list:
            final_list.append(word_one)

print(final_list)