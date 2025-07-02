class Circle:

    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):

        circumference = 2 * self.__pi * self.radius
        return circumference

    def calculate_area(self):

        area = self.__pi * (self.radius ** 2)
        return area

    def calculate_area_of_sector(self, angle):

        area_sector = (angle / 360) * self.__pi * (self.radius ** 2)
        return area_sector
