'''
print(4>3 and 5>1)

print(5<1 or 7>3)

print(9<1 and 1<3)

print(1>3 or 3<2)

list = (1,2,3,4)
print(4 in list)

print(4 not in list)

print(2<<3) # 2*2^3
print(4<<3) # 4*2^3

print(16>>3) # 16/2^3
print(32>>4) # 32/2^4

x=-2
if x>0:
  print('x is positive')
elif x<0:
  print('x is negative')
else:
  print('value is zero')

# calculater code
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice : "))

if choice == 1:
    print("The sum of", num1, "and", num2, "is", num1 + num2)
elif choice == 2:
    print("The difference between", num1, "and", num2, "is", num1 - num2)
elif choice == 3:
    print("The product of", num1, "and", num2, "is", num1 * num2)
elif choice == 4:
    print("The division of", num1, "by", num2, "is", num1 / num2)
else:
    print("Invalid choice")

for i in range(2,21,2):
    print(i)

list = [2,3,4,5,6]
sum = 0
for i in list:
    sum = sum+i
    print(sum)

c=0
while c<=10:
    print(c)
    c=c+1
else:
     print(f"value of c is {c}")

# skip,break,pass

for i in range(1,11):
   if i==5:
      continue   # to skip 5
   print(i)

for i in range(1,11):
   if i==5:
      break   # to break before 5
   print(i)


for i in range(1,11):
   if i==5:
      pass # to not get error(it act as a placeholder)
   print(i)

#function
def great(name,age):
     print(f"hello {name},{age}")
great('bhushan','21')


# to find avg temperature

weekly_temperatures = [25,27,28,26,24,30,29]

def avg(val):
    sum=0
    for i in val:
        sum += i
        avg = sum/len(val)
    print(f"the average is :{avg}")

avg(weekly_temperatures)


# to find cities having temperature less than 26

climate_data = [
    {"city": "City A", "temperature": 25, "carbon_footprint": 500},
    {"city": "City B", "temperature": 30, "carbon_footprint": 350},
    {"city": "City C", "temperature": 22, "carbon_footprint": 600},
    {"city": "City D", "temperature": 15, "carbon_footprint": 200},
    {"city": "City E", "temperature": 28, "carbon_footprint": 450},
]

for data in climate_data:
    if data["temperature"] > 26:
        print(data["city"])


#to find the avg carbon footprints

climate_data = [
    {"city": "City A", "temperature": 25, "carbon_footprint": 500},
    {"city": "City B", "temperature": 30, "carbon_footprint": 350},
    {"city": "City C", "temperature": 22, "carbon_footprint": 600},
    {"city": "City D", "temperature": 15, "carbon_footprint": 200},
    {"city": "City E", "temperature": 28, "carbon_footprint": 450},
]

total = 0
for data in climate_data:
    total += data["carbon_footprint"]

avg = total / len(climate_data)
print(avg)


climate_data = [
    {"city": "City A", "temperature": 25, "carbon_footprint": 500},
    {"city": "City B", "temperature": 30, "carbon_footprint": 350},
    {"city": "City C", "temperature": 22, "carbon_footprint": 600},
    {"city": "City D", "temperature": 15, "carbon_footprint": 200},
    {"city": "City E", "temperature": 28, "carbon_footprint": 450},
]

total = 0
for data in climate_data:
    total += data["carbon_footprint"]

avg = total / len(climate_data)

for data in climate_data:
 if data["carbon_footprint"] < avg:
   sustainable_cities = data["city"]
   print(sustainable_cities)

def calculate_carbon_footprint(energy_consumption, emission_factor, total_waste, ef_w):
  ec_cf = energy_consumption * emission_factor
  tw_cf = total_waste*ef_w
  return ec_cf + tw_cf

calculate_carbon_footprint(1000,0.475,6800,0.92)

'''
