# Program that asks the user for a total of 20
# numbers, adds them to an array and outputs
# sMax, min, AVG and Sum of the elements of the array.

#I only need ceil for this exercise due to the hotdogs
#and buns coming in packages. I promise, it will make sense later.


print("\n ##### Cosimo Morelli #####\n" + 
        " ## CS-115-OLA01-22FAACC ##\n" +
        " # Introduction to Python #\n" +
        " #######  W6 - Ex4  #######\n")
print("\nThis program calculates the number of packages of hotdog buns," +
      "\nhotdogs packages, hotdogs leftovers and hotdog buns leftovers" +
      "\ngiven a number of people and a number of hotdogs served for each.\n")  
numbers = []
total = 0
for i in range(20):
    number = int(input(f'({(i+1)}) Enter a whole number: '))
    numbers.append(number)
    total += number
print(" Max\tMin\tAVG\tTOT")
print(f" {max(numbers)}\t{min(numbers)}\t{total/20}\t{total}\t")
