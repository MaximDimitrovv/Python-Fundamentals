def already_in_collection_check(dictionary,new_piece_name):
    if new_piece_name in dictionary:
        return True
    else:
        return False

n = int(input())
pieces_info = {}

for _ in range(n):
    info = input().split("|")
    pieces_info[info[0]] = [info[1], info[2]]

while (line := input()) != "Stop":
    command = line.split("|")
    piece = command[1]
    is_in_dict = already_in_collection_check(pieces_info, piece)

    if command[0] == "Add":
        composer = command[2]
        key = command[3]
        if not is_in_dict:
            pieces_info[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command[0] == "Remove":
        if is_in_dict:
            pieces_info.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        if is_in_dict:
            new_key = command[2]
            pieces_info[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for k, v in pieces_info.items():
    composer = v[0]
    key = v[1]
    print(f"{k} -> Composer: {composer}, Key: {key}")