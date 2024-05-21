def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:

        mid = (low + high) // 2

        if target == lst[mid]:
            return mid
        elif target < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return None


lst = [4, 5, 6, 7, 8, 9, 10]

# set a target value
target_value = 7

result = binary_search(lst, target_value)

if result:
    print(f"Element {target_value} is found at index {result}")
else:
    print(f"{target_value} is not found in the list")
