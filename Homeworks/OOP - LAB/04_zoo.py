class Zoo:

    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        names = ''

        if species == "mammal":
            names = ', '.join(self.mammals)
            return f"Mammals in {self.zoo_name}: {names}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            names = ', '.join(self.fishes)
            return f"Fishes in {self.zoo_name}: {names}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            names = ', '.join(self.birds)
            return f"Birds in {self.zoo_name}: {names}\nTotal animals: {Zoo.__animals}"

zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())


for _ in range(n):
    line = input().split(" ")

    specie = line[0]
    name = line[1]

    zoo.add_animal(specie, name)

info = input()
print(zoo.get_info(info))

