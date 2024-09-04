# create 3 class
# vehicle
    # Vehicle info (Make, model, year)
    # Display Vehicle info
# car
    # car info (Number of doors)
    # disply carinfo
# electric car
    # electric car info(battery capacity )

# display()

# class Vehicle:
#     def vehicle_info (self,make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def display_vehicle_info(self):
#         print("Vehicle Make: ", self.make)
#         print("Vehicle Model: ", self.model)
#         print("Model Year: ", self.year)
# class Car(Vehicle):
#     def car_info (self,No_doors):
#         self.No_doors = No_doors
#     def display_car_info(self):
#         print("No of doors: ", self.No_doors)
# class ElectricCar(Car):
#     def electric_car_info(self, battery_capacity):
#         self.battery = battery_capacity
#     def display_electric_car_info(self):
#         print("Cattery Capacity: ", self.battery)
#     def display(self):
#         self.display_vehicle_info()
#         self.display_car_info()
#         self.display_electric_car_info()
# electric_car = ElectricCar()
# electric_car.vehicle_info("Tesla", "Model S", 2022)
# electric_car.car_info(4)
# electric_car.electric_car_info("100 kWh")
# electric_car.display()



# class Vehicle:
#     def __init__ (self,make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def display_vehicle_info(self):
#         print("Vehicle Make: ", self.make)
#         print("Vehicle Model: ", self.model)
#         print("Model Year: ", self.year)
# class Car(Vehicle):
#     def __init__ (self,make, model, year,No_doors):
#         Vehicle.__init__(self,make, model, year)
#         self.No_doors = No_doors
#     def display_car_info(self):
#         print("No of doors: ", self.No_doors)
# class ElectricCar(Car):
#     def __init__(self, make, model, year,No_doors, battery_capacity):
#         Car.__init__(self,make, model, year, No_doors)
#         self.battery = battery_capacity
#     def display_electric_car_info(self):
#         print("Cattery Capacity: ", self.battery)
#     def display(self):
#         self.display_vehicle_info()
#         self.display_car_info()
#         self.display_electric_car_info()
# electric_car = ElectricCar("Tesla", "Model S", 2022, 4, "100 kWh")
# electric_car.display()


class Vehicle:
    def __init__ (self,make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_vehicle_info(self):
        print("Vehicle Make: ", self.make)
        print("Vehicle Model: ", self.model)
        print("Model Year: ", self.year)
class Car(Vehicle):
    def __init__ (self,make, model, year,No_doors):
        super().__init__(make, model, year)
        self.No_doors = No_doors
    def display_car_info(self):
        print("No of doors: ", self.No_doors)
class ElectricCar(Car):
    def __init__(self, make, model, year,No_doors, battery_capacity):
        super().__init__(make, model, year, No_doors)
        self.battery = battery_capacity
    def display_electric_car_info(self):
        print("Cattery Capacity: ", self.battery)
    def display(self):
        self.display_vehicle_info()
        self.display_car_info()
        self.display_electric_car_info()
electric_car = ElectricCar("Tesla", "Model S", 2022, 4, "100 kWh")
electric_car.display()
