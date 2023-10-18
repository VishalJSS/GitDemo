class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

class Garage:
    def __init__(self, stored_car_class, brand, model, year):
        self.stored_car = stored_car_class(brand, model, year)

    def display_car_info(self):
        print(self.stored_car.get_info())

# Create a Garage object and pass the Car class as an argument
my_garage = Garage(Car, "Tesla", "Model S", 2018)

# Display the stored car's information
my_garage.display_car_info()

