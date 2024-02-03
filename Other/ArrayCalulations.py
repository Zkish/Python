import numpy as np

def Find_Duplicates(fullList):
    seen = set()
    duplicates = set()
    for numbers in fullList:
        if numbers in seen:
            duplicates.add(numbers)
        else:
            seen.add(numbers)
            continue
        return list(duplicates)

# Generaating random arrays
x = np.random.randint(1, 100, size = 50)
y = np.random.randint(1, 100, size = 50)

# Sorting arrays
Xlist = sorted(x)
Ylist = sorted(y)

# Combining arrays
fullList = Xlist + Ylist

# Calculations
Average = np.average(fullList)
Median = np.median(fullList)
Max = np.max(fullList)
Min = np.min(fullList)
Mode = Find_Duplicates(fullList)

# Outputs
print(Average)
print(Median)
print(Max)
print(Min)
print("Number or Numbers that occured the most:", Mode, "\n")
print(Xlist, "\n")
print(Ylist, "\n")

print(fullList)

exit()
