def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Comparamos las cadenas de texto en orden alfabético
            if str(arr[j]) > str(arr[j + 1]):
                # Realizamos el intercambio de elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

