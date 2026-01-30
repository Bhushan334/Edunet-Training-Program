'''
import numpy as np

# Energy consumption in MWh for different renewable sources: Solar, Wind, Hyd

ec = [1200, 3400, 2900, 1800, 2500] 
energy_consumption = np.array(ec)

# Print the array

print("Energy Consumption (in MWh) for Different Renewable Sources:")
print(energy_consumption)

import numpy as np
#Energy Consumption in MWh for different renewable  sources : solar , wind , hydro

ec=[1200,3400,2900,1800,2500]
energy_comnsumption=np.array(ec)

#printing the array
print("Energy Consumption (MWh) for different Renewable Sources:", energy_comnsumption)

A = np.ones(4)
A2 = np.ones((2, 2))
print(A)
print("\n", A2)


M = np.identity(4)
print("\nIdentity Matrix (4x4):\n", M)


import numpy as np
#Energy Consumption in MWh for different renewable  sources : solar , wind , hydro

ec=[1200,3400,2900,1800,2500]
energy_comnsumption=np.array(ec)

#printing the array
print("Energy Consumption (MWh) for different Renewable Sources:", energy_comnsumption)

A = np.ones(4)
A2 = np.ones((2, 2))
print(A)
print("\n", A2)


M = np.identity(4)
print("\nIdentity Matrix (4x4):\n", M)

#calculate the total energy consumption
total_consumption = np.sum(energy_comnsumption)

print(f"Total Energy Consumption (MWh): {total_consumption} MWh")


#calculate the mean average energy consumption
mean_consumption = np.mean(energy_comnsumption)
print(f"Mean Average Energy Consumption (MWh): {mean_consumption} MWh")


#calculate standard deviation of energy consumption
std_deviation = np.std(energy_comnsumption)
print(f"Standard Deviation of Energy Consumption (MWh): {std_deviation} MWh")


#reshape the array (to 5 rows and 1 column)
energy_comnsumption2= np.array([1200,3400,2900,1800,2500,1800])
reshaped_array = energy_comnsumption2.reshape(3, 2)
print("\nReshaped Energy Consumption Array (3x2):\n", reshaped_array)

#flatten the array
flattened_array = reshaped_array.flatten()
print("\nFlattened Energy Consumption Array:\n", flattened_array)

#transpose the array
# Method 1 : using .T (shortcut)
transposed_array = reshaped_array.T
print("\nTransposed Energy Consumption Array (2x3) using .T:\n", transposed_array)

# Method 2 : using np.transpose()
transposed_array_np = np.transpose(reshaped_array)
print("\nTransposed Energy Consumption Array (2x3) using np.transpose():\n", transposed_array_np)

resize_array = np.resize(reshaped_array,(3,3))
print("\nResized of Consumption Array:\n", resize_array)


# np.array(): Creates a NumPy array from a list or other iterable.
# np.random.randint(0, 10, 1): Generates a random integer between 0 and 10, with size 1.
# np.unique(): Finds the unique elements in an array and returns them in sorted order.
# np.dot(): Computes the dot product of two arrays or matrices.
# np.power(a, 2): Raises each element of array a to the power of 2.
# np.sqrt(a): Returns the square root of each element in the array a.
# np.ones(): Creates a new array of the specified shape, filled with ones.
# np.zeros(): Creates a new array of the specified shape, filled with zeros.
# np.max(): Returns the maximum value in the array.
# np.arange(10): Creates an array with evenly spaced values from 0 to 9.



import pandas as pd

#sample renewable energy source data

renewable_resources = ["solar", "wind", "hydro", "geothermal", "biomass"]

#create a series of renewable resources
resources_series = pd.Series(renewable_resources)

print("Renewable Energy Resources Series:")
print(resources_series)

'''
