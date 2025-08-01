def length_is_valid(username:str) -> bool:
    if 3 <= len(username) <= 16:
        return True
    return False

def characters_are_valid(username:str) -> bool:
    for character in username:
        if not(character.isalnum() or character == "-" or character == "_"):
            return False
    return True

def no_redundant_symbols(username:str) -> bool:
    if " " in username:
        return False
    return True

def username_is_valid(username:str) -> bool:
    if length_is_valid(username) and characters_are_valid(username) and no_redundant_symbols(username):
        return True

    return False

usernames_list = input().split(", ")
for username in usernames_list:

    if username_is_valid(username):
        print(username)