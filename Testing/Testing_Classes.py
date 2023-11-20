from Classes import Customer, Vehicle
C1 = Customer("Zachary Kish", 22, "3012 Belleville St")
C1_Car = Vehicle("Honda", "Accord", 2009, "Black")
C2 = Customer("Josh Kirsch", 23, "219 Fifth St")
C2_Car = Vehicle("Hyundai", "Elantra", 2015, "Grey")
C3 = Customer("Megan Harris", 21, "Greymill Drive")
C3_Car = Vehicle("Volkswagon", "Beatle", 2007, "Blue")
GetInfo = input("Enter The Name of Customer to View thier Information: ")
if GetInfo ==  "Zachary Kish":
    print("Here is Information about " + C1.name)
    print(C1.name, "Drives a", C1_Car.brand, C1_Car.make, C1_Car.color)
elif GetInfo == "Josh Kirsch":
    print("Here is Information about " + C2.name)
    print(C3.name, "Drives a", C2_Car.brand, C2_Car.make, C2_Car.color)
elif GetInfo == ("Megan Harris"):
    print("Here is Information about " + C3.name)
    print(C3.name, "Drives a", C3_Car.brand, C3_Car.make, C3_Car.color)