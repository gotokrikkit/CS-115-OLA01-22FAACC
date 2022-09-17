# A county collects property taxes on the assessment value of property, which is 60 percent of
# the property’s actual value. For example, if an acre of land is valued at $10,000, its assessment value
# is $6,000. The property tax is then 72¢ for each $100 of the assessment value.
# The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the
# actual value of a piece of property and displays the assessment value and property tax.

# This problem has 3 interpretation: continuous tax increment;
from math import ceil, floor
print("\n ##### Cosimo Morelli #####\n" +
      " ## CS-115-OLA01-22FAACC ##\n" +
      " # Introduction to Python #\n" +
      " #######  W4 - Ex5  #######\n")
print("\nThis program calculates assessment value and taxes" +
      "\nthat must be paid when a user input the nominal value" +
      "\nof a property with a setting of 72c for each $100 of the assessment value.\n")

# By now you should know I like to give the opportunity to
# users to run the program again, I hate to have to double click
# over and over to re-run something

# and fixed taxes (every $100)
# lower bound ([$0-$100] = 72c ... [$100.01-$200.00] = $1.44 ... etc)


def output():
    return print("\nAssessment value: ${:.2f}" +
                 "\nProperty tax: ${:.2f}" +
                 "\n\nDo you want to run the program again? [y/n] ").format(assessment, tax)


while True:
    # The only variable needed
    landvalue = float(input("What is the nominal value of the property? $"))

# Output for continuous increment, where every dollar is $0.072 taxes [ as in real life :( ]
    print(f"\nThe assessment value for the property is ${round((landvalue*.60),2)}" +                                           # I am nesting the computation rounded to 2 digits
          f"\n\tThe taxes that must be paid for the property amount to ${round((((landvalue*.60)/100)*0.72),2)}")               # Same as the previous line, it is ugly but
    # I follow Reverse Polish Notation, yes I am 41 :D

# Output with explanation for the fixed rate, just have fun with different amounts, like $15895 to see why I did it this way
    print("\nIn case of a fixed tax-rate, where the increment of taxes only occurs every $100:")

    # Same as the previous line, it is ugly but
    print(
        f"\tThe taxes that must be paid for the property amount to ${round(((floor((landvalue*.60)/100))*0.72),2)}")
    # I follow Reverse Polish Notation, yes I am 41 :D
    print("\nIn case of a lower bound tax-rate, where the increment of taxes only occurs inside ranges of $100:")

    # Same as the previous line, it is ugly but
    print(
        f"\tThe taxes that must be paid for the property amount to ${round(((ceil((landvalue*.60)/100))*0.72),2)}")
    # I follow Reverse Polish Notation, yes I am 41 :D
    if input("\nDo you want to run it again? [y] [n]: ") != 'y':
        print("\nSee you next time ! ! !\n")
        break
