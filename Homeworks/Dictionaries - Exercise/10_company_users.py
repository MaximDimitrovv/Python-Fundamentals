
info = {}

while (line := input()) != "End":
    company_name, employee_id = line.split(" -> ")

    if company_name not in info:
        info[company_name] = []

    if employee_id not in info[company_name]:
        info[company_name].append(employee_id)

for company_name, employee_id in info.items():
    print(f"{company_name}")
    for emp_id in employee_id:
        print(f"-- {emp_id}")