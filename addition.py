# Sum of n integers
def addition(a):
    sum = 0
    for i in a:
        sum += i
    return sum


a = [int(x) for x in input().split()]
result = addition(a)
print("sum of list =", result)
