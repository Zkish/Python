# this code will only work if executed outside of this repository so just fork it onto your local machine and 
# run it and then it will work.

# impports
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

# Calculations for ["Item Total"]
TotalSpent = df["Item Total"].sum()
AverageSpent = df["Item Total"].mean()
MostSpent = df["Item Total"].max()
LeastSpent = df["Item Total"].min()

# [Item Total] calculation outputs
print("Amount You Spent Overall: ", TotalSpent)
print("Average Spent Per Item: ", AverageSpent)
print("Most Spent On An Item: ", MostSpent)
print("Least Spent On An Item: ", LeastSpent)
print("if the least spent amount was 0 then that means that you used a gift card balance.")
print("\n")

# Calculating Savings on Sale Items
Savings = df["List Price Per Unit"].sum() - df["Purchase Price Per Unit"].sum()
print("The Amount of Money You Saved Buying Things on Sale: ", Savings)