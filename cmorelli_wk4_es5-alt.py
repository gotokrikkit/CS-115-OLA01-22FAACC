# A county collects property taxes on the assessment value of property, which is 60 percent of
# the property’s actual value. For example, if an acre of land is valued at $10,000, its assessment value
# is $6,000. The property tax is then 72¢ for each $100 of the assessment value.
# The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the
# actual value of a piece of property and displays the assessment value and property tax.

# Both needed for the multiple interpretation of the problem
from math import ceil, floor

print("\n ##### Cosimo Morelli #####\n" +
      " ## CS-115-OLA01-22FAACC ##\n" +
      " # Introduction to Python #\n" +
      " #######  W4 - Ex5  #######\n")
print("\nThis program calculates assessment value and taxes" +
      "\nthat must be paid when a user input the nominal value" +
      "\nof a property with a setting of 72c for each $100 of the assessment value.\n")


def assessment(input):  # Calculate the assessment value
    return round((input*.60), 2)


def taxes(input):
    # Calculate the taxes for the property
    taxes = round((((input*.60)/100)*0.72), 2)


def taxesfix(input):
    # Calculate the taxes for the property as fixed rate
    return round(((floor((input*.60)/100))*0.72), 2)


def taxesblock(input):
    # Calculate the taxes for the property as block bound
    return round(((ceil((input*.60)/100))*0.72), 2)


while True:  # While needed for asking the user if he wants to run the program again
    # The only variable needed, input the nominal value of the
    # property nested and attributed to the variable landvalue
    landvalue = float(input("What is the nominal value of the property? $"))

# Output for continuous increment, where every dollar is $0.072 taxes [ as in real life :( ]
    print(f"\nThe assessment value for the property is ${assessment(landvalue)}" +
          f"\n\tThe taxes that must be paid for the property amount to ${taxes(landvalue)}")               # Same as the previous line, it is ugly but
    # I follow Reverse Polish Notation, yes I am 41 :D

# Output with explanation for the fixed rate, just have fun with different amounts, like $15895 to see why I did it this way
    print("\nIn case of a fixed tax-rate, where the increment of taxes only occurs every $100:")

    print(
        f"\tThe taxes that must be paid for the property amount to ${taxesfix(landvalue)}")

    print("\nIn case of a lower bound tax-rate, where the increment of taxes only occurs inside ranges of $100:")

    print(
        f"\tThe taxes that must be paid for the property amount to ${taxesblock(landvalue)}")

    if input("\nDo you want to run it again? [y] [n]: ") != 'y':
        print("\nSee you next time ! ! !\n")
        break
