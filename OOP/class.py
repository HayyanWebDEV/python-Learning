
class vehicle():
    def __init__(self, vehicle):
        self.vehicle = vehicle
        print(f"i am a {vehicle}")
    def Vroomvroom(self):
        noise = "vroom" * 2
        return noise


car = vehicle("sports car")
car2 = vehicle("range rover")
print(car.vehicle)
print(car.Vroomvroom())