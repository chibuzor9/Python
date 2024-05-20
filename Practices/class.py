# CLasses

class Animal:
    def walk(self):
        print("Walking......")


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")


roger = Dog("Roger", 8)

print(roger.name)
print(roger.age)

roger.bark()
roger.walk()
