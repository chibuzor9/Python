def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


def merge(left, right):
    res = list()

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res


data_list = [1, 15, 6, 8, 2, 5, 9]

sorted_list = merge_sort(data_list)

print(sorted_list)
