# Task: Redo the program but with the use function.
# Task 1: Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Note: Define the function amount_Of_Money() and price_Of_Apple() then use return command to return the value of function. 
def amount_Of_Money():
    addInput1 = int(input("Enter amount of money: "))
    return addInput1
def price_Of_Apple():
    addInput2 = int(input("What is the price of apple? "))
    return addInput2
# Task 2: Display the maximum number of apples that you can buy and the remaining money that you will have.
# Note: Define the function compute() and use return command to return the value of function.
def compute():
    addFunc = int(amount/price)
    return addFunc
# Call the function of
amount = amount_Of_Money()
price = price_Of_Apple()
total = compute()
# Note: Define the function remaining() and use return command to return the value of function.
def remaining():
    balance = int(amount-(total*price))
    return balance
# Call the function of
balance = remaining()
# Task 3: Display the output in the following format.
def output(totalA, balanceB):
    print (f"You can buy {total} apples and your change is {balance} pesos.")
output(total, balance)
# Then, run the entire program.