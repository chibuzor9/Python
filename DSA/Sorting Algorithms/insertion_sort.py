def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]

        j = i - 1

        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]

            j -= 1

        lst[j + 1] = key

    return lst


# take integer inputs and convert it to a list
data_list = [1, 15, 6, 8, 2, 5, 9]

# call the insertion_sort() function
result = insertion_sort(data_list)

# print the sorted list
print(result)