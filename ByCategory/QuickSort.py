
def quick_sort_strings(arr, start, end):
    stack = [(start, end)]

    while stack:
        start, end = stack.pop()

        if start < end:
            p = partition(arr, start, end)
            stack.append((start, p - 1))
            stack.append((p + 1, end))

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1



