# Program to calculate the number of packages of hotdog buns,
# hotdogs packages, hotdogs leftovers and hotdog buns leftovers
# given a number of people and a number of hotdogs served for each.

# I only need ceil for this exercise due to the hotdogs
# and buns coming in packages. I promise, it will make sense later.
from math import ceil

print("\n ##### Cosimo Morelli #####\n" +
      " ## CS-115-OLA01-22FAACC ##\n" +
      " # Introduction to Python #\n" +
      " #######  W2 - Ex8  #######\n")
print("\nThis program calculates the number of packages of hotdog buns," +
      "\nhotdogs packages, hotdogs leftovers and hotdog buns leftovers" +
      "\ngiven a number of people and a number of hotdogs served for each.\n")

# The while is only to ask the user to run the program again

while True:
    people = int(input("Input number of people "))  # Only 2 variables needed
    # For the exercise
    hotdogs = int(input("Input hotdogs served per person "))

# Really all the next variables mandatory but I think you want us to show how to make use of what we learn

    # how many packages rounded up for hotdogs
    packsofbuns = ceil((people*hotdogs)/8)
    packsofdogs = ceil((people*hotdogs)/10)  # same but for the hotdog buns

    # how many individual buns left
    # Reversing the previous operation to get the number of buns left
    leftbuns = packsofbuns * 8 - (people * hotdogs)
    # how many individual hotdogs left
    # Reversing the previous operation to get the number of hotdogs left
    leftdogs = packsofdogs * 10 - (people * hotdogs)

    print(f"\nFor {people} people you need {packsofbuns} packs of buns and {packsofdogs} packages of hotdogs," +
          f"\nthere will be {leftbuns} single buns left and {leftdogs} single hotdogs left")

    if input("\nDo you want to run it again? [y] [n]: ") != 'y':
        print("\nSee you next time ! ! !\n")
        break
