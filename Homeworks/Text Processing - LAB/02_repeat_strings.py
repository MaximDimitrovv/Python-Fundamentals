string_list = input().split(" ")


print("".join([word * len(word) for word in string_list]))
