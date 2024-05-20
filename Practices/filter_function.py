# Filter Function
# Just like the map() function, it iterates thru a list but this checks
# whether the condition is True and then returns the True value.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def isEven(n):
    return n % 2 == 0
# isEven = lambda n: n % 2 == 0

result = list(filter(isEven, num))
# result = list(filter(lambda n: n % 2 == 0,num))

print(result)
