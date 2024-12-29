class House:
    def __init__(self, name, numberOfFloors=0):
        self.name = name
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

    def __eq__(self, other):
        if isinstance(other, House):
            return self.numberOfFloors == other.numberOfFloors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.numberOfFloors < other.numberOfFloors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.numberOfFloors <= other.numberOfFloors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.numberOfFloors > other.numberOfFloors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.numberOfFloors >= other.numberOfFloors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.numberOfFloors != other.numberOfFloors
        return True

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.numberOfFloors + value)
        elif isinstance(value, House):
            return House(self.name, self.numberOfFloors + value.numberOfFloors)
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.numberOfFloors}"


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)