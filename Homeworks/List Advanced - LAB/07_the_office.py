employee_happiness = input().split(" ")
factor = int(input())

mapped_list = []

for happiness in employee_happiness:
    num = int(happiness)
    mapped_list.append(num * factor)

average = sum(mapped_list) / len(mapped_list)

counter = 0
for number in mapped_list:
    if number >= average:
        counter += 1

if counter >= (len(mapped_list) / 2):
    print(f"Score: {counter}/{len(mapped_list)}. Employees are happy!")
else:
    print(f"Score: {counter}/{len(mapped_list)}. Employees are not happy!")