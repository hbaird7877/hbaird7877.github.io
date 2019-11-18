
def factorial():
    num = int(input("Enter a positive integer to calculate the factorial:"))
    a = isinstance(num, int)
    if (a == True and num >= 0):
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        print("The factorial of {} is {}.".format(num, fact))
    else:
        print("Please enter a positive integer")

factorial()
