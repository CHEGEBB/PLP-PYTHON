class Vehicle:
    """Base Vehicle class"""
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def move(self):
        """Base move method - should be overridden by subclasses"""
        print(f"{self.name} is moving")


class Car(Vehicle):
    """Car class that inherits from Vehicle"""
    
    def __init__(self, name, color, engine_type):
        super().__init__(name, color)
        self.engine_type = engine_type
    
    def move(self):
        """Override the move method for Car"""
        print(f"{self.color} {self.name} is driving on the road! 🚗")


class Boat(Vehicle):
    """Boat class that inherits from Vehicle"""
    
    def __init__(self, name, color, boat_type):
        super().__init__(name, color)
        self.boat_type = boat_type
    
    def move(self):
        """Override the move method for Boat"""
        print(f"{self.color} {self.name} is sailing across the water! 🚢")


class Plane(Vehicle):
    """Plane class that inherits from Vehicle"""
    
    def __init__(self, name, color, airline):
        super().__init__(name, color)
        self.airline = airline
    
    def move(self):
        """Override the move method for Plane"""
        print(f"{self.color} {self.name} from {self.airline} is flying through the sky! ✈️")


# Create different vehicle objects
toyota = Car("Corolla", "Red", "Hybrid")
sailboat = Boat("Voyager", "White", "Sailboat")
boeing = Plane("Boeing 747", "Blue", "United Airlines")

# Demonstrate polymorphism
print("Demonstrating polymorphism with different vehicles:")
print("-" * 45)

toyota.move()    # Car's version of move()
sailboat.move()  # Boat's version of move()
boeing.move()    # Plane's version of move()

# We can also use polymorphism with a list of vehicles
print("\nDemonstrating polymorphism using a list:")
print("-" * 45)

vehicles = [toyota, sailboat, boeing]

for vehicle in vehicles:
    # Each vehicle uses its own version of move()
    vehicle.move()