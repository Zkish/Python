GroceryList = []

for i in range(1, 11):
    item = GroceryList.append(input("Enter the items you need to get at the store:\n"))
    if i == 10:
        print("\n")
        print("here are the items that are in your finished grocery list:\n")
        for x in GroceryList:
            print(x)