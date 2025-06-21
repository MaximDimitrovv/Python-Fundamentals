current_version = input().split(".")

new_version = []
str_version = ""

for version in current_version:
    str_version += version

number = int(str_version)
number += 1

for last_version in str(number):
    new_version.append(last_version)

print(".".join(new_version))


