# Decorators
# As the name imply, they are used to wrap a function in them, it's like a
# function in function scenario.
# And they also always start with the '@' symbol followed by the decorator
# function's name.
# It's quite useful when you forget to add something and your code is very
# lengthy instead of making numerous adjustments you can just use it


def logtime(func):
    def wrapper():
        print("Before Func")
        val = func()
        print("After Func", end="\n\n")
        return val

    return wrapper


@logtime
def hello():
    print("Hello!")


@logtime
def my_name():
    print("Chibuzor Emmanuel")


hello()
my_name()
