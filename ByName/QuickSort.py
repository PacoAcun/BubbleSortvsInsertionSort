def quick_sort_strings(arr, start, end):
    size = end - start + 1
    stack = [0] * size
    top = -1

    top += 1
    stack[top] = start
    top += 1
    stack[top] = end

    while top >= 0:
        end = stack[top]
        top -= 1
        start = stack[top]
        top -= 1

        p = partition(arr, start, end)

        if p - 1 > start:
            top += 1
            stack[top] = start
            top += 1
            stack[top] = p - 1

        if p + 1 < end:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = end

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1
