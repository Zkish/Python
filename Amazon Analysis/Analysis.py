# this code will only work if executed outside of this repository so just fork it onto your local machine and 
# then extract the folder onto desktop outside of the Python directory / repo and then run it in VScode.

# imports
import pandas as pd

# importing the .csv file to be munipulated
filename = "amazon-orders.csv"
df = pd.read_csv(filename)

# gets rid of null values and replaces with 0's
df.fillna(0)

# changing string to float values so we can get number data calculations
# also getting rid of the # symbol as well
df["Item Total"] = df["Item Total"].str.replace('$', '').astype(float)
df["List Price Per Unit"] = df["List Price Per Unit"].str.replace('$', '').astype(float)
df["Purchase Price Per Unit"] = df["Purchase Price Per Unit"].str.replace('$', '').astype(float)
df["Item Subtotal Tax"] = df["Item Subtotal Tax"].str.replace('$', '').astype(float)
df["Order Date"] = df["Order Date"].str.replace('/', '').astype(float)
df["Order ID"] = df["Order ID"].str.replace('-', '').astype(str)

# data type variable containers after cleaning the data corresponding to the variables
a = df["Item Total"]
b = df["List Price Per Unit"]
c = df["Purchase Price Per Unit"]
d = df["Item Subtotal Tax"]
e = df["Order Date"]
f = df["Order ID"]
g = df["Title"]

# Calculations for ["Item Total"]
TotalSpent = a.sum()
AverageSpent = a.mean()
MostSpent = a.max()
LeastSpent = a.min()

# [Item Total] calculation outputs
print("\n")
print("Amount You Spent Overall: ", TotalSpent)
print("Average Spent Per Item: ", AverageSpent)
print("Most Spent On An Item: ", MostSpent)
print("Least Spent On An Item: ", LeastSpent)
print("\n")

# Calculating Savings on Sale Items
Savings = b.sum() - c.sum()
print("The Amount of Money You Saved Buying Things on Sale: ", Savings)
print("\n")

# Calculating Taxes on Item Totals
Taxes = d.sum()
print("Total Amount Spend On Taxes: ", Taxes)
print("\n")