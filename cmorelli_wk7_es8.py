print("\n ##### Cosimo Morelli #####\n" + 
        " ## CS-115-OLA01-22FAACC ##\n" +
        " # Introduction to Python #\n" +
        " #######  W7 - Ex8  #######\n")
print("\nThis program calculates the number of packages of hotdog buns," +
      "\nhotdogs packages, hotdogs leftovers and hotdog buns leftovers" +
      "\ngiven a number of people and a number of hotdogs served for each.\n") 
def make_it_capital(userinput):
    userinputLetters=[]
    userinputLetters[:0]=userinput
    userinputLetters[0]=userinputLetters[0].upper()
    stopLetters = ('...', '.', '?', '!', '!!!')
    for words in range(1,len(userinputLetters)-2):
        if userinputLetters[words] in stopLetters and userinputLetters[words+1]==' ':
            userinputLetters[words+2]=str(userinputLetters[words+2]).upper()
    return "".join(userinputLetters)
        

print(make_it_capital(input()))