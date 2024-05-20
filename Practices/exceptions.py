# Exceptions
# Here the syntax is so humane. You try some block of code and add exception
# errors.

try:
    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])
    # This causes an IdexError

    numerator = 10
    denominator = 0

    result = numerator / denominator
    # This causes a ZeroDivisionError
    print(result)
except IndexError:
    print("Index Out of Bound.")
else:
    print("Denominator cannot be 0.")
finally:
    print("Finally do this!")
