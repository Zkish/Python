# intro / choice maker
print("your calculator choices are: MinuteCalc, CelsiusToFahrenheit, and ")
choice = input("Which calculator would you like to use?\n")
# hours to minutes
if choice == "MinuteCalc":
    minutesInhour = 60
    hour = int(input("input the number of hours you want calculated into minutes:\n"))
    hoursTominutes = minutesInhour * hour
    print("here is how many minutes are in the number of hours that you specified:\n", hoursTominutes, " minutes")
    exit()
    # celsius to fahrenheit
elif choice == "CelsiusToFahrenheit":
    celsius = int(input("how much degrees is it in celsius?\n"))
    CtoF = celsius * 1.8 + 32
    print("Your celsius to Fahrenheit calculation would be: ", CtoF, " degrees fahrenheit.")
    exit()