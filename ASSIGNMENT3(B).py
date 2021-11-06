# Task: Redo the program but with the use function.
# Task 1: Create a program that will ask how many apples and oranges you want to buy.
# Note : Define the function appleAmount() and orangeAmount() then use return command to return the value of function.
def appleAmount():
    apple_User_Input = int(input("How many apples you want to buy? "))
    return apple_User_Input
def orangeAmount(): 
    orange_User_Input = int(input("How many oranges you want to buy? "))
    return orange_User_Input
# Call the function for
appleInput = appleAmount()
orangeInput =  orangeAmount()
# Task 2: Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Note : Define the function price_Of_Apple() and use the return command to return the value of apple to the function which is 20.
# the same way with the function price_Of_Orange() and use the return command to return the value of orange to the function which is 25.
def price_Of_Apple():
    apple = 20
    return apple
def price_Of_Orange():
    orange = 25
    return orange
# Call the function for 
applePrice = price_Of_Apple()
orangePrice = price_Of_Orange()
# Compute the total bill.
bill = int(appleInput*applePrice) + (orangeInput*orangePrice)
# Task 3: Display the output in the following format. The total amount is ________.
# Note : The print the total amount of the bill.
print ('The total amount is', bill)
# Lastly, run and debug the program to make sure that it is working!