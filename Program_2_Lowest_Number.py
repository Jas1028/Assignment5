# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

def AskNumber():
    Number1 = float(input("First number: "))
    Number2 = float(input("Second number: "))
    Number3 = float(input("Third number: "))
    return Number1, Number2, Number3

def LowestNumber(Number1_, Number2_, Number3_):
    if Number1_ < Number2_ and Number1_ < Number3_:
       print("The lowest number is",Number1_)
    else:
        if Number2_ < Number1_ and Number2_ < Number3_:
            print("The lowest number is", Number2_)
        else:
            if Number3_ < Number1_ and Number3_ < Number2_:
                print("The lowest number is",Number3_)
        




Number1, Number2, Number3 = AskNumber()
LowestNumber(Number1, Number2, Number3)