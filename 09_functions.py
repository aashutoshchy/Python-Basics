# Buil-in Functions
# print(), len(), type(), range()
# print("This is Built in function!")

# User-defined functions

# # Function definition
# def sum(firstNum, secNum): # Parameters
#     print("Sum is: ", firstNum + secNum)

# sum(4,5) #Function call, arguments


# Finding Average of three numbers
# Declaring Function
# def average(num1, num2, num3):
#     return ((num1 + num2 + num3) / 3)

# Taking Input From User
# num1 = int(input("Enter first Number: "))
# num2 = int(input("Enter second Number: "))
# num3 = int(input("Enter third Number: "))

# Printing Average
# average = average(num1, num2, num3)
# print("Average is: ", average)

# Default Parameter
# Calculating Product
# def calc_Prod(a=1, b=2):
#     print(a*b)

# calc_Prod()

# Practice Questions 1
# fruits = ["Apple", "Banana", "Litchi", "Mango", "Grapes"]
# games = ["Football", "Volleyball", "Badminton"]

# def printLength(list):
#     print("Length is", len(list))

# printLength(fruits)
# printLength(games)

# Practice Questions 2
# inst = ["Guitar", "Tambourine", "Piano", "Bass"]

# def printElm(list):
#     for item in list:
#         print(item, end=" ")

# printElm(inst)

# Practice Questions 3 // Factorial
# def findFact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact

# print("Factorial is: ", findFact(6))

# Practice Questions 4
def checkEvenOdd(n):
    if (n%2==0):
        print("Even")
    else:
        print("Odd")

num = int(input("Enter any number: "))
checkEvenOdd(num)