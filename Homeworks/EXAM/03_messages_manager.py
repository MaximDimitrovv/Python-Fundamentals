capacity = int(input())

messenger = {}


while (command := input()) != "Statistics":
    split_command = command.split("=")
    action = split_command[0]

    match action:
        case "Add":
            username = split_command[1]
            sent = int(split_command[2])
            received = int(split_command[3])

            if username not in messenger:
                messenger[username] = {"sent":sent, "received":received}
        case "Message":
            sender = split_command[1]
            receiver = split_command[2]

            if sender in messenger and receiver in messenger:
                messenger[sender]['sent'] += 1
                messenger[receiver]['received'] += 1

                if messenger[sender]['sent'] + messenger[sender]['received'] >= capacity:
                    messenger.pop(sender)
                    print(f"{sender} reached the capacity!")
                if messenger[receiver]['received'] + messenger[receiver]['sent'] >= capacity:
                    messenger.pop(receiver)
                    print(f"{receiver} reached the capacity!")
        case "Empty":
            username = split_command[1]
            if username != "All":
                messenger.pop(username)
            else:
                messenger.clear()

print(f"Users count: {len(messenger)}")

for name, data in messenger.items():
    sent = data["sent"]
    received = data["received"]
    print(f"{name} - {sent + received}")