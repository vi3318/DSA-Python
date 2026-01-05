# Object Oriented Programming 
from car import Car

# self is provided behind the scenes when we call methods on an object
car1 = Car("Toyota", 2024, "Red", True)
car2 = Car("Honda", 2025, "Blue", False)
car3 = Car("Ford", 2024, "Black", True)

print(car1)
print(car1.model)
print(car2.year)
print(car3.color)
print(car1.forSale)
