string = input()
rage_message = ""
current_text = ""
current_number = ""
collecting_number = False

for char in string:
    if not char.isdigit():
        if collecting_number:
            rage_message += current_text.upper() * int(current_number)
            current_text = ""
            current_number = ""
            collecting_number = False
        current_text += char
    else:
        collecting_number = True
        current_number += char

if current_text and current_number:
    rage_message += current_text.upper() * int(current_number)

unique_symbols = set(rage_message)

print(f"Unique symbols used: {len(unique_symbols)}")
print(rage_message)