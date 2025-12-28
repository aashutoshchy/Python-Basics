# List

num = [1, 2, 3, 4, 10]
# print(num)
# print(type(num))

# print(num[3])
# print(len(num))

# We can store elements of different types

std1 = ["Aashutosh", 19, "Kathmandu"]
# print(std1)

# Strings is immutable Lists is mutable i.e we can change value list

std1[1] = 20
# print(std1)

# List Slicing
# list_name = [starting_index : ending_index]

num1 = [23, 31, 12, 44, 54, 64]
# print(num1[2:5])


# num1.append(69)
# print(num1)

# list.sort() sort in ascending order.

# .insert(idx, el) insert element at index

# Practice Questions
# movList = []

# mov1 = input("Enter a movie: ")
# mov2 = input("Enter a movie: ")
# mov3 = input("Enter a movie: ")

# movList.append(mov1)
# movList.append(mov2)
# movList.append(mov3)

# print(movList)

list1 = [1,2,1, 3]

copyList = list1.copy()
copyList.reverse()

if list1 == copyList:
    print("Palindrome")
else:
    print("Not Palindrome")


