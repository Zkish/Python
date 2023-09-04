# Selection
selection = input("Would you like to open Savings or Budgeting? (S,B)?\n")
# After Selecting
if selection == "B":
    print("WELCOME TO YOUR BUDGET:\n")
    # income per month
    monthtlyIncome = int(input("how much do you make per month after taxes?\n"))
     # fixed expenses
    rent = int(input("Rent: "))
    monthtlyIncome = monthtlyIncome - rent
    print("total after this expense: ", monthtlyIncome)
    utilites = int(input("Utilites: "))
    monthtlyIncome = monthtlyIncome - utilites
    print("total after this expense: ", monthtlyIncome)
    car = int(input("car payment and insurance: "))
    monthtlyIncome = monthtlyIncome - car
    print("total after this expense: ", monthtlyIncome)
    insurance = int(input("other insurance: "))
    monthtlyIncome = monthtlyIncome - insurance
    print("total after this expense: ", monthtlyIncome)
    subscriptions = int(input("subscriptions: "))
    monthtlyIncome = monthtlyIncome - subscriptions
    print("total after this expense: ", monthtlyIncome)
    # variable expenses
    groceries = int(input("groceries: "))
    monthtlyIncome = monthtlyIncome - groceries
    print("total after this expense: ", monthtlyIncome)
    gasForcar = int(input("gas for car: "))
    monthtlyIncome = monthtlyIncome - gasForcar
    print("total after this expense: ", monthtlyIncome)
    entertainment = int(input("entertainment: "))
    monthtlyIncome = monthtlyIncome - entertainment
    print("total after this expense: ", monthtlyIncome)  
    eatingOut = int(input("eating out: "))
    monthtlyIncome = monthtlyIncome - eatingOut
    print("total after this expense: ", monthtlyIncome)
    badHabits = int(input("bad habits: "))
    monthtlyIncome = monthtlyIncome - badHabits
    print("total after this expense: ", monthtlyIncome)
    randomShopping = int(input("random things throughout the month: "))
    monthtlyIncome = monthtlyIncome - randomShopping
    print("total after this expense: ", monthtlyIncome)
    # savings
    longTerm = int(input("long term savings: "))
    monthtlyIncome = monthtlyIncome - longTerm
    print("total after this expense: ", monthtlyIncome)
    shortTerm = int(input("short term savings: "))
    monthtlyIncome = monthtlyIncome - shortTerm
    print("total after this expense: ", monthtlyIncome)
    investments = int(input("investments: "))
    monthtlyIncome = monthtlyIncome - investments
    print("total after this expense: ", monthtlyIncome)
    # total / leftover
    # afterAll = # add in here something that will show how much was overages or how much money is leftover after all the expenses.
    print("after all expenses you have this much left over or this much you need to adjust with your budget: ", monthtlyIncome)