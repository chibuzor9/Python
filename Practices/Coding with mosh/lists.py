names = ["John", "Bob", "Mosh", "Sam", "Mary"]
names[0] = "Jon"
print(names[0:3])
print(names)

#List Methods
numbers = [1,2,3,4,5]
numbers.insert(1,6)
numbers.remove(4)

#numbers.clear()

print(numbers)
print(4 in numbers)

print("Length: " + str(len(numbers)))