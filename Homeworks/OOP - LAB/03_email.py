class Email:
    def __init__(self, sender, receiver, content, is_send= False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = is_send

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"

all_emails = []

while True:

    message = input()
    if message == "Stop":
        indexes = list(map(int, input().split(", ")))

        for index in range(len(all_emails)):
            sender_name = all_emails[index][0]
            receiver_name = all_emails[index][1]
            content_message = all_emails[index][2]

            if index in indexes:
                sent = Email(sender_name, receiver_name, content_message)
                sent.send()
                print(sent.get_info())
            else:
                sent = Email(sender_name, receiver_name, content_message)
                print(sent.get_info())

        break
    else:
        all_emails.append(message.split(" "))

