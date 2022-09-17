from math import ceil, floor

print("\n ##### Cosimo Morelli #####\n" +
      " ## CS-115-OLA01-22FAACC ##\n" +
      " # Introduction to Python #\n" +
      " #######  W4 - Ex5  #######\n")
print("\nThis program calculates assessment value and taxes" +
      "\nthat must be paid when a user input the nominal value" +
      "\nof a property with a setting of 72c for each $100 of the assessment value.\n")

# This problem has 3 interpretation: continuous tax increment; fixed rate lower bound; fixed rate block range


def total_taxes(landvalue):  # Defines the function and the input
    # Raw computation of the assessment value
    assessment = round((landvalue*.60), 2)
    # Raw computation of the taxes
    taxes = round(((assessment/100)*0.72), 2)
    # Raw computation of the taxes with fixed rate
    taxfix = round(((floor(assessment/100))*0.72), 2)
    # Raw computation of the taxes with fixed rate
    taxblock = round(((ceil(assessment/100))*0.72), 2)
    print(f"\nThe assessment value for the property is ${assessment} for what the taxes are ${taxes}\n" +  # Output
          f"\nIn case of a fixed tax-rate, the taxes owed are: ${taxfix}" +
          f"\nIn case of a lower bound rate, the taxes owed are: ${taxblock}")


# the while is only to ask the user to run the program again
while True:
    total_taxes(
        float(input("Plese insert the nominal value of the property: $")))

    if input('\nDo you want to run it again? [y] [n]: ') != 'y':
        print("\nSee you next time ! ! !\n")
        break
