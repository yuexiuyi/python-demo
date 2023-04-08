import Car
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    

car = ElectricCar('tesla', 'model s', 2016)
print(car.get_descriptive_name())