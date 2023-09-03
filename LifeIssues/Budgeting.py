# Selection
selection = input("Would you like to open Savings or Budgeting? (S,B)?\n")
# After Selecting
if selection == "B":
    print("WELCOME TO YOUR BUDGET:\n")
    # income per month
    monthtlyIncome = int(input("how much do you make per month after taxes?\n"))
     # fixed expenses
    rent = int(input("Rent: "))
    after = monthtlyIncome - rent
    print("total after this expense: ", after)
    utilites = int(input("Utilites: "))
    after = monthtlyIncome - rent - utilites
    print("total after this expense: ", after)
    car = int(input("car payment and insurance: "))
    after = monthtlyIncome - rent - utilites - car
    print("total after this expense: ", after)
    insurance = int(input("other insurance: "))
    after = monthtlyIncome - rent - utilites - car - insurance
    print("total after this expense: ", after)
    subscriptions = int(input("subscriptions: "))
    after = monthtlyIncome - rent - utilites - car - insurance - subscriptions
    print("total after this expense: ", after)
    # variable expenses
    groceries = int(input("groceries: "))
    after = monthtlyIncome - rent - utilites - car - insurance - subscriptions - groceries
    print("total after this expense: ", after)
    gasForcar = int(input("gas for car: "))
    after = monthtlyIncome - rent - utilites - car - insurance - subscriptions - groceries - gasForcar
    print("total after this expense: ", after)
    entertainment = int(input("entertainment: "))
    after = monthtlyIncome - rent - utilites - car - insurance - subscriptions - groceries - gasForcar - entertainment 
    print("total after this expense: ", after)  
    eatingOut = int(input("eating out: "))
    after = monthtlyIncome - rent - utilites - car - insurance - subscriptions - groceries - gasForcar - entertainment - eatingOut
    print("total after this expense: ", after)
    badHabits = int(input("baf habits: "))
    after = monthtlyIncome - rent - utilites - car - insurance - subscriptions - groceries - gasForcar - entertainment - eatingOut - badHabits
    print("total after this expense: ", after)
    randomShopping = int(input("random things throughout the month: "))
    after = monthtlyIncome - rent - utilites - car - insurance - subscriptions - groceries - gasForcar - entertainment - eatingOut - badHabits - randomShopping
    print("total after this expense: ", after)
    # savings
    longTerm = int(input("long term savings: "))
    after = monthtlyIncome - rent - utilites - car - insurance - subscriptions - groceries - gasForcar - entertainment - eatingOut - badHabits - randomShopping - longTerm
    print("total after this expense: ", after)
    shortTerm = int(input("short term savings: "))
    after = monthtlyIncome - rent - utilites - car - insurance - subscriptions - groceries - gasForcar - entertainment - eatingOut - badHabits - randomShopping - longTerm - shortTerm
    print("total after this expense: ", after)
    investments = int(input("investments: "))
    after = monthtlyIncome - rent - utilites - car - insurance - subscriptions - groceries - gasForcar - entertainment - eatingOut - badHabits - randomShopping - longTerm - shortTerm - investments
    print("total after this expense: ", after)
    # total / leftover
    # afterAll = # add in here something that will show how much was overages or how much money is leftover after all the expenses.
    print("after all expenses you have this much left over or this much you need to adjust with your budget: ", afterAll)