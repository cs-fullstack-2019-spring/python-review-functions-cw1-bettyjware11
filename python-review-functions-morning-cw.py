def main():
    #Problem1()
     Problem2()


# Create a function that has a loop
# Prompt for numbers until the user enters q to quit
# If the user doesn't enter q, ask them to input another number
# When the user enters q to quit, print the SUM of all numbers entered
def Problem1():
    userInput = int(input("Enter a number or enter 'q' to quit"))
    userInputPrint = ""

    while (userInput != 'q'):
        userInputPrint = int(userInput) + int(userInput)
        userInput = input("Enter another or q to quit ")
    print(userInputPrint)

#Example: Dictionary result returned if the argumants 25 and 10 are passed to the function:
#{'diff': 15, 'prod': 250, 'quot': 2.5, 'sum': 35}
#In your problem2() function, print the dictionary result returned from
# your do_the_math function using string literal formatting

#Create a function Problem 2...
def Problem2():
#In this function prompt the user for 2 numbers
num1 = int(input("Enter number"))
num2 = int(input("Enter number"))
#Create a second function called do_the_math that accepts 2 parameters (the 2 entered numbers)
def do_the_math(num1,num2):
#In the do_the_math calculate the SUM, DIFFERENCE, PRODUCT,
# and QUOTIENT (division result) and return them as a dictionary to the calling function
    SUM = num1 + num2
    DIFFERENCE = num1 - num2
    PRODUCT = num1 * num2
    QUOTIENT = num1 / num2
    myDictionaryList = [{SUM(num1,num2)}, {DIFFERENCE(num1,num2)},
    {PRODUCT(num1,num2)}, {QUOTIENT(num1,num2)}]




if __name__ == '__main__':
    main()
