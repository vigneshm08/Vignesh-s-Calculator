print ("Welcome to Vignesh's Calculator")
print ("Do you want to perform addition of 2 numbers?")
ask_addition = input('Enter y or n\n')

if ask_addition == "y":
    print ("Cool then. Let's get started")
    i = 1
    while i > 0:

        try:
            num1 = float(input("enter the first number:"))
            num2 = float(input("enter the second one:"))


            res = num1 + num2
            res2 = int(res)
            print("the sum is " + str(res2))
            print("do you want perform another calculation?")
            again = input ("Enter y or n\n")
            if again == "y":
                i = i + 1
            else:
                i = 0
                print("thanks for using Vignesh's Calculator. See you again next time!")

        except :
            print ("enter an integer")
else:
    print("Then you must looking to do something else that is not ready yet")
    feedback = input ("Please type out what you are looking for. We will add it to our list")
