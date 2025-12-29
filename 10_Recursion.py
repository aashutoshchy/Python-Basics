# Recursive function
# def show(n):
#     if (n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# Finding Factorial
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return fact(n-1) * n
    
# print(fact(5))

def find_sum(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    return find_sum(n-1) + n

print(find_sum(5))


