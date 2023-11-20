# My Functions Page

# removing duplicates
def remove_duplicates(lst):
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list

# count occurences of elements in a list
def count_elements(lst):
    element_count = {}
    for element in lst:
        element_count[element] = element_count.get(element, 0) + 1
    return element_count

# adding numbers
def add_numbers(x, y):
    result = x + y
    print(result)
    return result

# subtracting numbers
def subtract_numbers(x, y):
    result = x - y
    print(result)
    return result

# dividing numbers
def divide_numbers(x, y):
    result = x / y
    print(result)
    return result

# DataReader Function
def datareader(file):
    for x in file:
        print(x)

# Find Length of  a String
def Find_length(input_string):
    length = len(input_string.replace(" ", ""))
    print(length)
    return length