# Simple program to convert temperatures from/to different systems [C]/[F]
# And repeat multiple times based on users choices

print("\n ##### Cosimo Morelli #####\n" +
      " ## CS-115-OLA01-22FAACC ##\n" +
      " # Introduction to Python #\n" +
      " #######  W1 - Ex9  #######\n")
print("This program converts temperatures from F-->C and/or C-->F\n")

# Set to one to prevent the program from closing immediately
# due to the while loop
easter_egg = 0
usrinput = 1
# Sets the exception for the program to keep running
while (usrinput > 0):

    # Prompt for the user to make a choice
    usrinput = int(input("Input: \n[1]: To convert To Fahrenheit [C->F];" +
                         "\n[2]: To convert To Celsius; [F->C]" +
                         "\n[0]: To Quit this Program;\n"))

# Quit choice
    if usrinput == 0:
        print("\nOk, come back any time\n")
        break
# First choice
    elif usrinput == 1:
        c2f = float(input("\nInput your temperature in Celsius: "))
        Fahrenheit = (c2f * 9/5) + 32

        print("\nThe %.2f degree Celsius corresponds to: %.2f Fahrenheit\n"
              % (c2f, Fahrenheit))
# Second choice
    elif usrinput == 2:

        f2c = float(input("\nInput your temperature in Fahrenheit: "))
        celsius = (f2c - 32) / (9/5)

        print("\nThe %.2f degree Fahrenheit corresponds to: %.2f Celsius\n"
              % (f2c, celsius))

# If the user types a different choice from the ones offered
    elif usrinput > 2:
        print("\nSorry it is either 1, 2 or 0\n")
    # variable for multiple answers
    easter_egg = easter_egg + 1
    if easter_egg == 3:
        print("1... 2... or 0\n")
    elif easter_egg == 6:
        print("OOOOOOOneee or TWWWWOOoooo or ZEEEERrooo\n")
    elif easter_egg == 9:
        print("That is NOT HOW THIS PROGRAM WORKS ! ! !\n")
    elif easter_egg == 12:
        print("Shall we play a game?\n")
    elif easter_egg == 15:
        print("Let me put it this way. The 9000 Series is the most reliable computer ever made.\n")
        continue
    if easter_egg == 20:
        print("I'm sorry, Dave. I'm afraid I can't do that\n")
        break
