
string_1 = input()
string_2 = input()

string_3 = list(string_1)


for i in range(len(string_2)):
    if string_2[i] != string_1[i]:
        string_3[i] = string_2[i]
        print("".join(string_3))
