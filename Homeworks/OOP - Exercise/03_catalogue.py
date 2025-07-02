class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [word for word in self.products if word.startswith(first_letter)]

    def __repr__(self):
        return f"Items in the {self.name} catalogue:\n" + "\n".join(sorted(self.products))
