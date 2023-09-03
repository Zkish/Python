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