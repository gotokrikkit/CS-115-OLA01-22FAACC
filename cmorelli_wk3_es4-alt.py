# this program converts feet to inches
# and inches to feet
def inches(feet):
    return feet * 12


def feet(inches):
    return inches / 12


def menu():  # prints the menu
    print("""
    1. Convert feet to inches
    2. Convert inches to feet
    3. Quit
    """)


menu()
if input == "1":
    print(inches(float(input("Enter the number of feet: "))))
elif input("Enter your choice: ") == "2":
    print(feet(float(input("Enter the number of inches: "))))
elif input("Enter your choice: ") == "3":
    print("Goodbye!")
    input("Press enter to exit")
