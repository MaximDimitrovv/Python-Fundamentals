string = input()


for i in range(len(string)):
    if string[i] == ":":
        print(f"{string[i]}{string[i+1]}")