from Classes import *
Customer1 = Customer("Zachary", 21 , "3012 belleville st")
Customer1_Car = Vehicle("Honda", "Accord", 2009, "Black")
GetInfo = input("Enter name of customer to get information on: \n")
if GetInfo == Customer1.name:
    print("here is information about " + Customer1.name)
    print(Customer1.name, "Drives a ", Customer1_Car.brand, Customer1_Car.make, Customer1_Car.year, Customer1_Car.color)
else:
    exit()
# Customer (name, age, address)
# Vehicle (brand, make, year, color)