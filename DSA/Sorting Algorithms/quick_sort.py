def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    left = []
    right = []

    pivot = lst.pop()

    for num in lst:
        if num > pivot:
            right.append(num)
        else:
            left.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)


# take integer inputs and convert it to a list
data_list = [1, 15, 6, 8, 2, 5, 9]


sorted_list = quick_sort(data_list)
print(sorted_list)
