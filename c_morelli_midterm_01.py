print("\n ##### Cosimo Morelli #####\n" +
      " ## CS-115-OLA01-22FAACC ##\n" +
      " # Introduction to Python #\n" +
      " #######  MID - P1  #######\n")
# Requirements as per the assignment:
# - Same As For the Course Exercises

tuition = float(8000)    # tuition amount predetermined
year = 0                    # year counter
print(f"\nFor a tuition of $ {tuition:,.2f} "  # print tuition amount with the right format for currency
      "the following is the tuition for the next 5 years:\n")
while year < 5:  # I did not set the year to 6 because the first year is already
    year += 1  # included in the tuition amount so I only need to add 5 years
    # to the tuition amount and multiply for 1.03 or 3% as requested
    tuition = tuition * 1.03
    # print the result with the right
    print(f"On year {year} the tuition will be ${round((tuition), 2):,.2f}")
    # format and round it to 2 decimals                                      #format for currency
