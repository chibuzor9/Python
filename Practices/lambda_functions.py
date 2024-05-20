# Lambda Functions are used to run simple expressions as functions

a = int(input("Your first Number "))
b = int(input("Your second Number "))

multiple = lambda a, b: a * b

print(f"\nYour multiple is {multiple(a,b)}")
