# Activity 2: Polymorphism Challenge! 🎭

class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        pass  # To be implemented by subclasses

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def move(self):
        pass  # To be implemented by subclasses

# Animal subclasses
class Dog(Animal):
    def move(self):
        return f"{self.name} is running! "

class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming! "

class Bird(Animal):
    def move(self):
        return f"{self.name} is flying! "

class Snake(Animal):
    def move(self):
        return f"{self.name} is slithering! "

# Vehicle subclasses
class Car(Vehicle):
    def move(self):
        return f"{self.brand} car is driving! "

class Plane(Vehicle):
    def move(self):
        return f"{self.brand} plane is flying! "

class Boat(Vehicle):
    def move(self):
        return f"{self.brand} boat is sailing! "

class Bicycle(Vehicle):
    def move(self):
        return f"{self.brand} bicycle is pedaling! "

# Function that demonstrates polymorphism
def make_it_move(movable_objects):
    print(" Let's make things move! ")
    print("-" * 40)
    
    for obj in movable_objects:
        print(obj.move())
    print()

# Create some animals
buddy = Dog("Buddy")
nemo = Fish("Nemo")
tweety = Bird("Tweety")
slither = Snake("Slither")

# Create some vehicles
toyota = Car("Toyota")
boeing = Plane("Boeing")
yacht = Boat("Luxury")
schwinn = Bicycle("Schwinn")

# Group 1: All animals
animal_group = [buddy, nemo, tweety, slither]

# Group 2: All vehicles
vehicle_group = [toyota, boeing, yacht, schwinn]

# Group 3: Mixed animals and vehicles
mixed_group = [buddy, toyota, nemo, boeing, slither, schwinn]

# Demonstrate polymorphism
print("=== ANIMALS MOVING ===")
make_it_move(animal_group)

print("=== VEHICLES MOVING ===")
make_it_move(vehicle_group)

print("=== MIXED GROUP MOVING ===")
make_it_move(mixed_group)

# Bonus: Interactive example
print(" BONUS: Interactive Movement Demo!")
movable_items = animal_group + vehicle_group

for i, item in enumerate(movable_items, 1):
    if isinstance(item, Animal):
        print(f"{i}. {item.name} ({item.__class__.__name__})")
    else:
        print(f"{i}. {item.brand} ({item.__class__.__name__})")

try:
    choice = int(input("\nChoose an item to move (1-8): "))
    if 1 <= choice <= len(movable_items):
        selected = movable_items[choice - 1]
        print(f"\n {selected.move()}")
    else:
        print("Invalid choice!")
except ValueError:
    print("Please enter a valid number!")