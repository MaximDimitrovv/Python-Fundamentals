number = int(input())
total_liters = 0

for _ in range(number):
    new_pour = int(input())

    if total_liters + new_pour <= 255:
        total_liters += new_pour
    else:
        print("Insufficient capacity!")

print(total_liters)
