import re

n = int(input())
pattern = r'^@[#]{1,}([A-Z][A-Za-z\d]{4,}[A-Z])@[#]{1,}$'

for _ in range(n):
    barcode = input()

    matches = re.findall(pattern, barcode)

    if matches:
        for match in matches:
            barcode = ''
            for letter in match:
                if letter.isdigit():
                    barcode += letter
            if not barcode:
                barcode = "00"

            print(f"Product group: {barcode}")
    else:
        print('Invalid barcode')