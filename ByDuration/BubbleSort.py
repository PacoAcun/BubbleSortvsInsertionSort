def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap arr[j] and arr[j+1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

