class Vehicle:

    wheels = 4
    fuel = "diesel"

    def __init__(self, time_to_100km_h, max_speed):
        self.time_to_100km_h = time_to_100km_h
        self.max_speed = max_speed


    def get_info(self):
        print(f"Up to 100km/h reaches the run in {self.time_to_100km_h} per second\n"
              f"maximum speed is {self.max_speed} km/h")

class BMV(Vehicle):
    def __init__(self, time_to_100km_h, max_speed, color):
        Vehicle.__init__(self, time_to_100km_h, max_speed)
        self.color = color


    def acceleration(self):
        return "10m/s2"

    def get_info(self):
        print(f"Up to 100km/h reaches the run in {self.time_to_100km_h} per second\n"
              f"maximum speed is {self.max_speed} km/h\n"
              f"color is {self.color}")


class Mercedes(Vehicle):
    def __init__(self, time_to_100km_h, max_speed, year_of_production):
        Vehicle.__init__(self, time_to_100km_h, max_speed)
        self.year_of_production = year_of_production

    def get_info(self):
        print(f"Up to 100km/h reaches the run in {self.time_to_100km_h} per second\n"
              f"maximum speed: {self.max_speed} km/h\n"
              f"Year of production: {self.year_of_production}")

    def acceleration(self):
        return "10.5m/s2"

class Bus(Vehicle):

    wheels = 8
    fuel = "Hydrogen"

    def __init__(self,  time_to_100km_h, max_speed, number_of_sets):
        Vehicle.__init__(self, time_to_100km_h, max_speed)
        self.number_of_sets = number_of_sets

        def acceleration(self):
            return "5m/s2"

    def get_info(self):
        print(f"Up to 100km/h reaches the run in {self.time_to_100km_h} per second\n"
              f"maximum speed is {self.max_speed} km/h\n"
              f"Number of sets {self.number_of_sets}")



car_BMW = BMV(5, 260, "Red")
car_Merc = Mercedes(5.5, 250, 2021)
bus = Bus(12.5, 180, 26)
print(car_BMW.time_to_100km_h)
print(car_Merc.max_speed)
print(car_Merc.wheels)
print(car_BMW.acceleration())
print(bus.wheels)
print(bus.fuel)
print(bus.get_info())
print(car_BMW.get_info())
print(car_Merc.get_info())

