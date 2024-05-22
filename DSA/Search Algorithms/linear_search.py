def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index

    return None


lst = [9, 10, 5, 8, 7, 4, 11, 6, 15, 3]

# take integer input to search in the list
target_value = int(input())

result = linear_search(lst, target_value)
print(result)
