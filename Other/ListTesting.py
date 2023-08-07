# creating the empty list.
names = []

# loop so that once the list items hit 10 then it will exit the loop.
for i in range(1, 11):
    person = names.append(input("what is the name of the first person in the list?\n"))
    print(names)
    if i == 10:
        print("\n")
        print("here is the final made list:\n", names)
        break