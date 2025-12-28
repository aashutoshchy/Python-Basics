# Set is the collection of the unorderred items.
# Each element in the set must be unique & immutable.

# collection = {1, 2, 3, 4, 3}
# print(collection) #Ignores Duplicate values
# print(type(collection))

# emptySet = set() #Syntax for creating Empty Set

# Set Methods
# Remember: Set is mutable but Its elements are Immutable
# We can't add mutable value in set like List

# collection = set()

# Add Method
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add("Aashutosh")

# print(collection)

# Remove Method
# collection.remove(3)
# print(collection)

# Union Method
set1 = {1, 2, 3, 4, 5, 6}
set2 = {2, 4, 6, 8}

print(set1.union(set2)) # Returns new value

# Intersection Method
print(set1.intersection(set2))