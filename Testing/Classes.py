# customer class
class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# vehicle class
class Vehicle:
    def __init__(self, brand, make, year, color):
        self.brand = brand
        self.make = make
        self.year = year
        self.color = color

# Budgeting Classes
class FixedSpending:
    def __init__(self, rent, utilities, subscriptions, insurance):
        self.rent = rent
        self.utilities = utilities
        self.subscriptions = subscriptions
        self.insurance = insurance

class FlexibleSpending:
    def __init__(self, gas, entertainment, eatingOut, badHabits):
        self.gas = gas
        self.entertainment = entertainment
        self.badHabits = badHabits
        self.eatingOut = eatingOut

class Savings:
    def __init__(self, longTerm, ShortTerm, Emergency):
        self.longTerm = longTerm
        self.ShortTerm = ShortTerm
        self.Emergency = Emergency