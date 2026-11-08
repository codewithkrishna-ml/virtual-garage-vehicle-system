#PROJECT-Virtual Garage & Vehicle System
class Vehicle:
    def __init__(self , brand , model , speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed +=10

    def show_status(self):
        print(f"vehicle brand:{self.brand} | Model: {self.model}|Current speed {self.speed}")

class Car(Vehicle):
    def __init__(self, brand, model, speed, doors):
        super().__init__(brand, model, speed)
        self.doors = doors

    def accelerate(self):
        self.speed +=20

class Bike(Vehicle):
    def __init__(self, brand, model, speed , has_carrier):
        super().__init__(brand, model, speed)
        self.has_carrier = has_carrier

    def accelerate(self):
        self.speed +=15

class Garage:
    def __init__(self):
        self.vehicle = []

    def add_vehicle(self , vehicle_object):
        self.vehicle.append(vehicle_object)

    def show_all(self):
        for v in self.vehicle:
            v.show_status()

garage = Garage()
garage.add_vehicle(Car("BMW", "M5", 10, 4))
garage.add_vehicle(Bike("Yamaha", "R15", 5, False))

for v in garage.vehicle:
    v.accelerate()

garage.show_all()
