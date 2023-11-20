def Find_length(input_string):
    length = len(input_string.replace(" ", ""))
    return length

print(Find_length("Hello World"))
print(Find_length("what is going on everyone"))
print(Find_length("a b c d e f g h i j k l m n o p q r s t u v w x y z "))