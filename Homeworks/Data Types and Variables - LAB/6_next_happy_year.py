year = int(input())
year += 1

while True:
    string_year = str(year)

    if len(set(string_year)) == len(string_year):
        print(year)
        break

    year += 1