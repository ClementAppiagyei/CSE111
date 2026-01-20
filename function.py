def function_name(param1, param2, paramN):
    """documentation string"""
    height = float(param2)
    length = float(param1)
    width = float(paramN)

    value = length * height * width
    return value


# get the three values first
length = input("What is the length of the table? ")
height = input("What is the height of the table? ")
width = input("What is the width of the table? ")

# call the function ONCE with all three values
value = function_name(length, height, width)

print(f"The volume of the table is {value}")
