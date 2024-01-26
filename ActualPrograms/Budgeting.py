monthlyIncome = int(input("Enter Your Monthly Income: "))
Fixed_Expense = []
Fixed_Costs = []
Variable_Expenses = []
Variable_Costs = []
i = 1
k = int(input("Enter Number of Fixed Expenses: "))
j = 1
l = int(input("Enter Number of Variable Expenses: "))
while i <= k:
    i += 1
    fixed = input("Enter Name of Expense: ")
    Fixed_Expense.append(fixed)
    fcost = int(input("Enter Cost of Expense: "))
    Fixed_Costs.append(fcost)
    continue
while j <= l:
    j += 1
    variable = input("Enter Name of Variable Expense: ")
    Variable_Expenses.append(variable)
    vcost = int(input("Enter Cost of Variable Expense: "))
    Variable_Costs.append(vcost)
    continue
Total = sum(Fixed_Costs + Variable_Costs)
Leftover = monthlyIncome - Total
print(f"Your Total Monthly Expenses Are: ${Total}\nYou have ${Leftover} Leftover After All Expenses Paid.")
