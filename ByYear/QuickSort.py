import sys

def quick_sort(arr, start, end):
    sys.setrecursionlimit(10**6)

    def quick_sort_helper(arr, start, end):
        while start < end:
            p = partition(arr, start, end)
            if p - start < end - p:
                quick_sort_helper(arr, start, p - 1)
                start = p + 1
            else:
                quick_sort_helper(arr, p + 1, end)
                end = p - 1

    quick_sort_helper(arr, start, end)

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


