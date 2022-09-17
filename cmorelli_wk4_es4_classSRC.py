class Taxes:
    global x
    x = input(" Dog: ")

    def __init__(self, name, breed, color, age):
        landvalue = input("What is the nominal value of the property? $")
        self.assessment = round((self.landvalue*.60), 2)
        self.taxes = round((((self.landvalue*.60)/100)*0.72), 2)
        self.taxesfix = round(((floor((self.landvalue*.60)/100))*0.72), 2)
        self.taxesblock = round(((ceil((self.landvalue*.60)/100))*0.72), 2)


def askUser():
    if (x != 0):
        print(f"landvalue: {dog1.name}")
        print(f"taxes: {dog1.breed}")
        print(f"taxesfix: {dog1.color}")
        print(f"taxesblock: {dog1.age}")
    elif (x == "dog2"):
        print(f"Name: {dog2.name}")
        print(f"Breed: {dog2.breed}")
        print(f"Color: {dog2.color}")
        print(f"Age: {dog2.age}")
    elif (x == "dog3"):
        print(f"Name: {dog3.name}")
        print(f"Breed: {dog3.breed}")
        print(f"Color: {dog3.color}")
        print(f"Age: {dog3.age}")
    else:
        print("No match")


dog1 = Dog('Jim', 'Shep', 'Brown', 6)
dog2 = Dog('Jimmy', 'Lab', 'Black', 5)
dog3 = Dog('Jimo', 'Dane', 'Black', 3)
askUser()
