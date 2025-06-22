
chat = []

while True:

    command = input()

    if command == "end":
        for message in chat:
            print(message)
        break

    split_command = command.split(" ")
    message = split_command[1]

    if "Chat" in command:
        chat.append(message)

    if "Delete" in command:
        if message in chat:
            chat.remove(message)

    if "Edit" in command:
        edited_version = split_command[2]
        for i in range(len(chat)):
            if chat[i] == message:
                chat[i] = edited_version

    if 'Pin' in command:
        if message in chat:
            chat.remove(message)
            chat.append(message)

    if 'Spam' in command:
        for text in split_command:
            if text != 'Spam':
                chat.append(text)

