# Dictionaries are used to store data values in key:value pairs
# They are unordered, mutable(changeable) & don't allow duplicate keys

# info = {
#     "name" : "Aashutosh Chaudhary",
#     "subjects" : ["Python", "JavaScript"],
#     "age" : 19,
#     "is_adult" : True
# }

# print(type(info))

# To access dictionary
# print(info["name"])
# print(info["subjects"])
# print(info["age"])
# print(info["is_adult"])

# To assign new value
# info["name"] = "Harry" # Overwrite original value
# print(info["name"])

# We can create empty dictionary
# empty_dict = {}
# print(empty_dict)

# To add value to null dictionary
# empty_dict["name"] = "Merry"
# print(empty_dict)

# To create nested dictionary

student = {
    "name": "Aashutosh Chy",
    "subjects": {
        "Introductory Programming And Problem Solving " : 99,
        "Fundamentals of Computing": 95,
        "Internet Software Architecture": 100
    }
}

# print(student)
# print(student["subjects"])
# print(student["subjects"]["Internet Software Architecture"])

# .keys() method
# print(student.keys())

# Converting keys into list
# print(list(student.keys()))
# print(len(list(student.keys())))

# .value() method
# print(student.values())

# .items() method
# print(tuple(student.items()))

# .get("key")
# print(student["name2"]) #give error
# print(student.get("name"))

# student.update({"City" : "Kathmandu", "age" : 19})
# print(student)

# Practice Questions
# Question 1
# dict1 = {
#     "table" : ["A Piece of furniture", "list of facts & figures"],
#     "cat" : "A Small Animal"
# }

# print(dict1)

# Question 2
FOC = float(input("Enter marks in FOC: "))
ISA = float(input("Enter marks in ISA: "))
PYTHON = float(input("Enter marks in PYTHON: "))

marks = {
    "FOC" : FOC,
    "ISA" : ISA,
    "PYTHON" : PYTHON
}

print(marks)