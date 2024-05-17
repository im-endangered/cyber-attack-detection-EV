class Car:
    def __init__(self, make, model, year, engine_type, horsepower, torque, speed=0, acceleration=0):
        self.make = make
        self.model = model
        self.year = year
        self.engine_type = engine_type
        self.horsepower = horsepower
        self.torque = torque
        self.speed = speed
        self.acceleration = acceleration

    def accelerate(self, amount):
        self.acceleration += amount

    def brake(self, amount):
        self.acceleration -= amount

    def update_speed(self):
        self.speed += self.acceleration

    def get_info(self):
        return f"{self.year} {self.make} {self.model}, Engine Type: {self.engine_type}, Horsepower: {self.horsepower}, Torque: {self.torque}, Speed: {self.speed}, Acceleration: {self.acceleration}"