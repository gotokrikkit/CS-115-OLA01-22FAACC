print("\n ##### Cosimo Morelli #####\n" +
      " ## CS-115-OLA01-22FAACC ##\n" +
      " # Introduction to Python #\n" +
      " #######  MID - P2  #######\n")
# Requirements as per the assignment:
# - Same As For the Course Exercises
# - Mandatory use of 1 or more functions
# - No fancy stuff, just the basics


def feet_to_inches(feet):   # function to convert feet to inches
    return round(feet * 12, 2)  # return the result of the conversion with
    # the right format and round it to 2 decimals
    # that is the same as inches = feet * 12


feet = float(
    input("Enter feet to be converted to inches: "))  # input feet to be converted
# print the result of the conversion and call the function feet_to_inches
print(f"\nThere are {feet_to_inches(feet)} inches in {feet} feet")
# inside the print function to convert the input feet to inches
