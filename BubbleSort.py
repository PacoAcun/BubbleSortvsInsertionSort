def bubble_sort(arr):
    n = len(arr)

    # Recorremos la lista n veces
    for i in range(n):
        swapped = False  # Un indicador para verificar si se realizaron intercambios en esta pasada
        # Recorremos la lista de 0 a n-i-1
        for j in range(0, n - i - 1):
            # Comparamos el elemento actual con el siguiente
            if arr[j] > arr[j + 1]:
                # Realizamos el intercambio de elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Si no se realizó ningún intercambio en esta pasada, la lista está ordenada
        if not swapped:
            break
