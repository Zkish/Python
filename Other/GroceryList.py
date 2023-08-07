# empty list.
GroceryList = []
# loop to add 10 items to the grocery list you can adjus this in the range.
for i in range(1, 11):
    item = GroceryList.append(input("Enter the items you need to get at the store:\n"))
    # if the list hits 10 in this case it will end the loop and move on to the next.
    if i == 10:
        print("\n")
        print("here are the items that are in your finished grocery list:\n")
        # this loop will print out each item that is in the list to give you a finalized overview of the items in the list.
        for x in GroceryList:
            print(x)