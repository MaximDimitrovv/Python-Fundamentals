def letter_case(text, command):
    if command == "Lower":
        return text.lower()
    elif command == "Upper":
        return text.upper()

def reverse(text, start_index, end_index):
    string = text[start_index:end_index + 1]
    return string[::-1]

def replace(text, char):
    string = ""
    for letter in text:
        if not letter == char:
            string += letter
        else:
            string += '-'
    return string

def substring(text, sub):
    if sub in text:
        new_text = text.replace(sub, '')
        return new_text
    else:
        return f"The username {text} doesn't contain {sub}."

def is_valid(text, char):
    if char not in text:
        return False
    else:
        return True

username = input()


while "Registration" not in (line := input().split()):

    if "Letters" in line:
        command = line[1]
        username = letter_case(username, command)
        print(username)

    elif "Reverse" in line:
        start_index = int(line[1])
        end_index = int(line[2])
        if start_index >= 0 and end_index < len(username):
            print(reverse(username, start_index, end_index))

    elif "Replace" in line:
        char = line[1]
        username = replace(username, char)
        print(username)

    elif "Substring" in line:
        sub = line[1]
        username = substring(username, sub)
        print(username)

    elif "IsValid" in line:
        char = line[1]

        if is_valid(username, char):
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")
