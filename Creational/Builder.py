class Car:
    def __init__(self):
        self.seats = None
        self.engine = None
        self.gps = None

    def __str__(self):
        return f"Car with {self.seats} seats, {self.engine} engine, and GPS: {self.gps}"

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_seats(self, seats):
        self.car.seats = seats

    def set_engine(self, engine):
        self.car.engine = engine

    def set_gps(self, gps):
        self.car.gps = gps

# Example usage
builder = CarBuilder()
builder.set_seats(4)
builder.set_engine("V6")
builder.set_gps(True)

car = builder.car
print(car)
