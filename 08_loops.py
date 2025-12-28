# While Loop

# Print Numbers from 1 to 100
# i = 1

# while i <= 100:
#     print(i)
#     i += 1


# Print Numbers from 100 to 1
# i = 100
# while i >= 1: #Stoping condition
#     print(i)
#     i -= 1

# Print Multiplication of n
# n = int(input("Enter any number: "))
# i = 1
# while i <= 10:
#     print(f"{n} X {i} = {n*i}")
#     i += 1


# i = 1
# j = 1
# while i <= 100:
#     print(i)
#     j += 2
#     i += j

# Break
# i = 1
# while i<= 5:
#     print(i)
#     if (i==3):
#         break
#     i = i +1

# Continue
# i = 1
# while i<= 5:
#     print(i)
#     if (i==3):
#         continue
#     i = i + 1

# For Loop
# nums = [1, 2, 3, 4, 5]
# for val in nums:
#     print(val)

# tup = (1,2,3,4,5)
# for num in tup:
#     print(num)

# str = "Ashutosh"
# for char in str:
#     print(char)

# Searching for an element
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# idx = 0
# x = 9

# for el in nums:
#     if (el == x):
#         print("Element found at: ", idx)
#     idx += 1



# range()
# Syntax: range(start?, stop, step?)
# Step is optional, default is 1

# for i in range(1, 101):
#     print(i)


# for i in range(100, 0, -1):
#     print(i)

# Sum of first n numbers. (using while)
# n = 5
# sum = 0

# while n > 0 :
#     sum += n
#     n -= 1

# print(sum)

n = 5
fact = 1
for i in range(1, n+1):
    fact *= i

print("Factorial is: ", fact)

