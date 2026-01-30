'''
#__init__() is used to build or set up your object when you create it
class EnergySystem:
    def __init__(self, building_name, energy_consumption, emission_factor):
        # Initialize attributes
        self.building_name = building_name
        self.energy_consumption = energy_consumption # in kWh
        self.emission_factor = emission_factor # in kg CO2 per kWh

    def calculate_carbon_footprint(self):
        return self.energy_consumption * self.emission_factor

    def display_info(self):
        print(f"Building Name: {self.building_name}")
        print(f"Energy Consumption: {self.energy_consumption} kWh")
        print(f"Emission Factor: {self.emission_factor} kg CO2 per kWh")

#method to calculate energy saving(Assume saving 10% for now)
    def calculate_energy_saving(self):
        return self.energy_consumption * 0.10

# Example usage
building = EnergySystem("Building A", 5000, 0.45)
building.display_info()
footprint = building.calculate_carbon_footprint()
energysaving = building.calculate_energy_saving()
print(f"Carbon Footprint: {footprint} kg CO2")
print(f"Energy Saving: {energysaving} kWh")


# Inheritance

#__init__() is used to build or set up your object when you create it
class EnergySystem:
    def __init__(self, building_name, energy_consumption, emission_factor):
        # Initialize attributes
        self.building_name = building_name
        self.energy_consumption = energy_consumption # in kWh
        self.emission_factor = emission_factor # in kg CO2 per kWh

    def calculate_carbon_footprint(self):
        return self.energy_consumption * self.emission_factor

    def display_info(self):
        print(f"Building Name: {self.building_name}")
        print(f"Energy Consumption: {self.energy_consumption} kWh")
        print(f"Emission Factor: {self.emission_factor} kg CO2 per kWh")

#method to calculate energy saving(Assume saving 10% for now)
    def calculate_energy_saving(self):
        return self.energy_consumption * 0.10

# Example usage
building = EnergySystem("Building A", 5000, 0.45)
building.display_info()
footprint = building.calculate_carbon_footprint()
energysaving = building.calculate_energy_saving()
print(f"Carbon Footprint: {footprint} kg CO2")
print(f"Energy Saving: {energysaving} kWh")


#subclass for SolarEnergySystem inheriting from EnergySystem
class SolarEnergySystem(EnergySystem):
    def __init__(self, building_name, energy_consumption, emission_factor, solar_capacity):
        # Call the constructor of the parent class
        super().__init__(building_name, energy_consumption, emission_factor)
        self.solar_capacity = solar_capacity # in kW

    #method to calculate net energy consumption after solar contribution
    def calculate_net_energy_consumption(self):
        solar_contribution = self.calculate_solar_contribution()
        return self.energy_consumption - solar_contribution

    def calculate_solar_contribution(self):
        # Assume solar contribution is 20% of energy consumption for simplicity
        return self.energy_consumption * 0.20

    def display_info(self):
        super().display_info()
        print(f"Solar Capacity: {self.solar_capacity} kW")

#Example useage of subclass
solar_building = SolarEnergySystem("Building B", 8000, 0.45, 50)
solar_building.display_info()
net_consumption = solar_building.calculate_net_energy_consumption()
solar_contribution = solar_building.calculate_solar_contribution()
print(f"Solar Contribution: {solar_contribution} kWh")
print(f"Net Energy Consumption: {net_consumption} kWh")


# Encapsulation

class EnergySystem:
  def __init__(self, building_name, energy_consumption, emission_factor):
    self.building_name = building_name
    self._energy_consumption = energy_consumption
    self._emission_factor = emission_factor

  def get_energy_consumption(self):
    return self._energy_consumption

  def calculate_carbon_footprint(self):
    return self._energy_consumption * self._emission_factor


B1 = EnergySystem("Building A", 5000, 0.45)

print(f"{B1.building_name} : {B1.get_energy_consumption()} kWh, {B1._emission_factor} kg CO2/kWh")


#Polymorphism

#__init__() is used to build or set up your object when you create it
class EnergySystem:
    def __init__(self, building_name, energy_consumption, emission_factor):
        # Initialize attributes
        self.building_name = building_name
        self.energy_consumption = energy_consumption # in kWh
        self.emission_factor = emission_factor # in kg CO2 per kWh

    def calculate_carbon_footprint(self):
        return self.energy_consumption * self.emission_factor

    def display_info(self):
        print(f"Building Name: {self.building_name}")
        print(f"Energy Consumption: {self.energy_consumption} kWh")
        print(f"Emission Factor: {self.emission_factor} kg CO2 per kWh")

#method to calculate energy saving(Assume saving 10% for now)
    def calculate_energy_saving(self):
        return self.energy_consumption * 0.10

# Example usage
building = EnergySystem("Building A", 5000, 0.45)
building.display_info()
footprint = building.calculate_carbon_footprint()
energysaving = building.calculate_energy_saving()
print(f"Carbon Footprint: {footprint} kg CO2")
print(f"Energy Saving: {energysaving} kWh")


#subclass for SolarEnergySystem inheriting from EnergySystem
class SolarEnergySystem(EnergySystem):
    def __init__(self, building_name, energy_consumption, emission_factor, solar_capacity):
        # Call the constructor of the parent class
        super().__init__(building_name, energy_consumption, emission_factor)
        self.solar_capacity = solar_capacity # in kW

    #method to calculate net energy consumption after solar contribution
    def calculate_net_energy_consumption(self):
        solar_contribution = self.calculate_solar_contribution()
        return self.energy_consumption - solar_contribution

    def calculate_solar_contribution(self):
        # Assume solar contribution is 20% of energy consumption for simplicity
        return self.energy_consumption * 0.20

    def display_info(self):
        super().display_info()
        print(f"Solar Capacity: {self.solar_capacity} kW")

#Example useage of subclass
solar_building = SolarEnergySystem("Solar Building ", 5000, 0.45, 1500)
solar_building.display_info()
net_consumption = solar_building.calculate_net_energy_consumption()
solar_contribution = solar_building.calculate_solar_contribution()
print(f"Solar Contribution: {solar_contribution} kWh")
print(f"Net Energy Consumption: {net_consumption} kWh")


#Encapsulation example
print("\nEncapsulation Example:")
class EncapsulatedEnergySystem:
    def __init__(self, building_name, energy_consumption, emission_factor):
        self.__building_name = building_name
        self.__energy_consumption = energy_consumption
        self.__emission_factor = emission_factor

    def calculate_carbon_footprint(self):
        return self.__energy_consumption * self.__emission_factor

    def get_building_name(self):
        return self.__building_name

    def set_energy_consumption(self, energy_consumption):
        if energy_consumption >= 0:
            self.__energy_consumption = energy_consumption
        else:
            print("Energy consumption cannot be negative.")

#example usage of encapsulation
encapsulated_building = EncapsulatedEnergySystem("Encapsulated Building", 5000, 0.45)
print(f"Building Name: {encapsulated_building.get_building_name()}")

#Polymorphism example
print("\nPolymorphism Example:")
class SolarEnergySystem(EnergySystem):
    def __init__(self, building_name, energy_consumption, emission_factor, solar_production):
        super().__init__(building_name, energy_consumption, emission_factor)
        self.solar_production = solar_production

    #overriding the carbon footprint method to account for Solar contribution
    def calculate_carbon_footprint(self):
        net_consumption = self.energy_consumption - self.solar_production
        return net_consumption * self.emission_factor

#example usage of polymorphism 
solar_building = SolarEnergySystem("Solar Building", 5000, 0.45, 1500)
solar_building.display_info()


# Smart Energy Consumption Analyzer

CRITICAL_GRID_LIMIT = 2000  # kWh

def calculate_total_and_average(consumptions):
    total = sum(consumptions)
    average = total / len(consumptions)
    return total, average

buildings = int(input("Enter number of buildings: "))

energy_data = []
total_consumption = 0

print("\nEnter hourly energy consumption (kWh):")

for i in range(buildings):
    consumption = float(input(f"Building {i+1}: "))
    energy_data.append(consumption)
    total_consumption += consumption

    if total_consumption > CRITICAL_GRID_LIMIT:
        print("\n⚠️ Critical Grid Limit Exceeded!")
        break

total, average = calculate_total_and_average(energy_data)

print("\n--- Sustainability Report ---")

for i, consumption in enumerate(energy_data):
    if consumption < 100:
        status = "Energy Efficient"
    elif consumption <= 300:
        status = "Moderate Consumption"
    else:
        status = "Energy Intensive"

    print(f"Building {i+1}: {consumption} kWh → {status}")

print(f"\nTotal Energy Consumption: {total:.2f} kWh")
print(f"Average Energy Consumption: {average:.2f} kWh")




# Base Class
class EnergySource:
    def __init__(self, name, power_output):
        self.name = name
        self.__power_output = power_output  # Encapsulation

    def get_power_output(self):
        return self.__power_output

    def calculate_availability(self):
        # To be overridden (polymorphism)
        return 0


# Derived Classes
class Solar(EnergySource):
    def calculate_availability(self):
        # Solar depends on sunlight (assume 70% efficiency)
        return self.get_power_output() * 0.7


class Wind(EnergySource):
    def calculate_availability(self):
        # Wind depends on speed (assume 60% efficiency)
        return self.get_power_output() * 0.6


class Hydro(EnergySource):
    def calculate_availability(self):
        # Hydro is stable (assume 90% efficiency)
        return self.get_power_output() * 0.9


# Decision Engine
sources = [
    Solar("Solar", 500),
    Wind("Wind", 400),
    Hydro("Hydro", 600)
]

print("---- Smart Grid Energy Allocation ----")

for hour in range(1, 6):  # simulate 5 time slots
    print(f"\nHour {hour}")

    best_source = None
    max_energy = 0

    for source in sources:
        available_energy = source.calculate_availability()

        if available_energy > max_energy:
            max_energy = available_energy
            best_source = source

    print(f"Selected Source: {best_source.name}")
    print(f"Energy Supplied: {max_energy:.2f} kWh")

'''
