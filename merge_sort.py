unsorted = [503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 612, 677, 765, 703]
odd = [1, 3, 5, 7]
even = [2, 4, 6, 8, 10, 12]


def merge_sort(aaa, bbb):
    result = []

    while len(aaa) > 0 and len(bbb) > 0:
        if aaa[0] < bbb[0]:
            result.append(aaa.pop(0))
        else:
            result.append(bbb.pop(0))

    if len(aaa) == 0:
        result = result + bbb
    else:
        result = result + aaa
    return result


def sort(arr):
    if len(arr) == 1:
        return arr
    else:
        middle = len(arr)//2
        return merge_sort(sort(arr[0:middle]), sort(arr[middle:len(arr)]))

print sort(unsorted)
print merge_sort(odd, even)