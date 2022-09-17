# Program to calculate the distance of a train given the speed and the time traveled,
# or then breaking down each hour the distance traveled.

print("\n ##### Cosimo Morelli #####\n" +
      " ## CS-115-OLA01-22FAACC ##\n" +
      " # Introduction to Python #\n" +
      " #######  W2 - Ex8  #######\n")
print("\nThis program calculates the distance of a train given the speed and the time traveled\n" +
      "\nfor then breaking down each hour the distance traveled.")

while True:                                 # This is the while loop for repeating the program
    ### Set the variables ###
    # this is used for the incremental of the while loop
    i = 1
    # Constant [physically speaking] for the speed
    speed = int(input(f"\nInsert the speed of the train in miles/h: "))
    # Time traveled by the train
    time = int(input(f"Insert the time traveled by train in hours: "))

    ### Headers for the output ###
    # I use unicode here because a bunch of lines take too much memory
    print("\n\x1B[4m"+"Hour           Distance Traveled"+"\x1B[0m")

    while (i <= time):  # Condition needed to print all the numbers
        # nice (in my opinion) format for the output with tabulation
        distance = speed*i
        print(f" {i} \t\t {distance} miles")
        i += 1

    if input("\nDo you want to run it again? [y] [n]: ") != 'y':
        print("\nSee you next time ! ! !\n")
        break
