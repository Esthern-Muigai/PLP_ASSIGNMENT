class Superhero:
    def __init__(self, name, power, weakness):
        self.name = name
        self.__power = power  # Private attribute
        self.__weakness = weakness  # Private attribute

    def display_info(self):
        print(f"Superhero Name: {self.name}")
        print(f"Power: {self.__power}")
        print(f"Weakness: {self.__weakness}")

    def change_weakness(self, new_weakness):
        self.__weakness = new_weakness

# Inheriting the Superhero class
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, weakness, flight_speed):
        super().__init__(name, power, weakness)
        self.flight_speed = flight_speed

    def display_info(self):
        super().display_info()
        print(f"Flight Speed: {self.flight_speed} km/h")

# Usage
hero = FlyingSuperhero("Sky Saver", "Flying", "Thunderstorms", 500)
hero.display_info()
hero.change_weakness("Rain")
print("\nAfter changing weakness:")
hero.display_info()


#Activity 2: Polymorphism Challenge! 
class Vehicle:
    def move(self):
        pass  # Base class defines the method but no implementation

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Usage
vehicles = [Car(), Plane(), Boat()]

print("Vehicle Actions:")
for v in vehicles:
    v.move()
