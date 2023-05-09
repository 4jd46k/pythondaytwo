class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} {self.model} starting... Vroom Vroom!")


class ElectricCar(Car):
    def start(self):
        print(f"{self.make} {self.model} starting... Zoom Zoom! It's electric!")


my_car = Car("Toyota", "Corolla")
my_car.start()  

my_electric_car = ElectricCar("Tesla", "Model S")
my_electric_car.start() 
