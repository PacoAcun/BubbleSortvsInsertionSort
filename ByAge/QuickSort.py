def quick_sort(arr, start, end):
    stack = [(start, end)]

    while stack:
        start, end = stack.pop()

        if start < end:
            p = partition(arr, start, end)
            stack.append((start, p - 1))
            stack.append((p + 1, end))

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1

        while arr[right] >= pivot and right >= left:
            right = right - 1

        if right < left:
            done = True
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

    temp = arr[start]
    arr[start] = arr[right]
    arr[right] = temp

    return right


