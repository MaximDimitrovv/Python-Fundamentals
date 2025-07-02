class Party:
    pass

    def __init__(self):
        self.people = []

    def add_people(self, people):
        self.people.append(people)

invited = Party()

while True:
    command = input()

    if command == "End":
        names = ", ".join(invited.people)

        print(f"Going: {names}")
        print(f"Total: {len(invited.people)}")
        break

    invited.add_people(command)
