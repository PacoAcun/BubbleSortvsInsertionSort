import pandas as pd
import time
import matplotlib.pyplot as plt
import random
import InsertionSort as ins
import BubbleSort as bub
import QuickSort as qck
import MergeSort as mrg

# Función para eliminar duplicados de una lista
def eliminate_duplicates(categories):
    unique_categories = []
    for category in categories:
        if category not in unique_categories:
            unique_categories.append(category)
    return unique_categories

df = pd.read_csv("Netflix DB.csv")

print("By category :")
print()

# Copia la columna "Category" en una lista para ordenarla
categories = df["Category"].astype(str).tolist()

# Lista preordenada
sorted_categories = sorted(categories)

# Lista preordenada de forma revertida
reverse_sorted_categories = sorted(categories, reverse=True)

# Lista preordenada de forma aleatoria
random_categories = random.sample(categories, len(categories))

# Mide el tiempo de ejecución de Insertion Sort para la lista preordenada
start_time = time.time()
ins.insertion_sort(sorted_categories)
end_time = time.time()
insertion_sort_time_sorted = end_time - start_time

# Mide el tiempo de ejecución de Insertion Sort para la lista preordenada de forma revertida
start_time = time.time()
ins.insertion_sort(reverse_sorted_categories)
end_time = time.time()
insertion_sort_time_reverse = end_time - start_time

# Mide el tiempo de ejecución de Insertion Sort para la lista preordenada de forma aleatoria
start_time = time.time()
ins.insertion_sort(random_categories)
end_time = time.time()
insertion_sort_time_random = end_time - start_time

# Mide el tiempo de ejecución de Insertion Sort para la lista ordenada
start_time = time.time()
ins.insertion_sort(categories)
end_time = time.time()
insertion_sort_time_normal = end_time - start_time

# Guardar el tiempo de ejecución en una lista
insertion_sort_time = [insertion_sort_time_normal, insertion_sort_time_reverse, insertion_sort_time_random, insertion_sort_time_sorted]

# Crea un DataFrame con la columna "Category" ordenada y sin duplicados
unique_categories = eliminate_duplicates(categories)
category_df_ins = pd.DataFrame(unique_categories, columns=["Category"])
category_df_ins.to_csv("ByCategory/Insertion.csv", index=False)

print(f"--------Tiempo de ejecución de Insertion Sort normal: {insertion_sort_time_normal} segundos-----------")
print(f"--------Tiempo de ejecución de Insertion Sort revertido: {insertion_sort_time_reverse} segundos-----------")
print(f"--------Tiempo de ejecución de Insertion Sort aleatorio: {insertion_sort_time_random} segundos-----------")
print(f"--------Tiempo de ejecución de Insertion Sort ordenado: {insertion_sort_time_sorted} segundos-----------")
print()


# Vuelve a cargar el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Copia la columna "Category" en una lista para ordenarla
categories = df["Category"].astype(str).tolist()

# Lista preordenada
sorted_categories = sorted(categories)

# Lista preordenada de forma revertida
reverse_sorted_categories = sorted(categories, reverse=True)

# Lista preordenada de forma aleatoria
random_categories = random.sample(categories, len(categories))

# Mide el tiempo de ejecución de Bubble Sort para la lista preordenada
start_time = time.time()
bub.bubble_sort(sorted_categories)
end_time = time.time()
bubble_sort_time_sorted = end_time - start_time

# Mide el tiempo de ejecución de Bubble Sort para la lista preordenada de forma revertida
start_time = time.time()
bub.bubble_sort(reverse_sorted_categories)
end_time = time.time()
bubble_sort_time_reverse = end_time - start_time

# Mide el tiempo de ejecución de Bubble Sort para la lista preordenada de forma aleatoria
start_time = time.time()
bub.bubble_sort(random_categories)
end_time = time.time()
bubble_sort_time_random = end_time - start_time

# Mide el tiempo de ejecución de Bubble Sort para la lista ordenada
start_time = time.time()
bub.bubble_sort(categories)
end_time = time.time()
bubble_sort_time_normal = end_time - start_time

# Guardar el tiempo de ejecución en la lista
bubble_sort_time = [bubble_sort_time_normal, bubble_sort_time_reverse, bubble_sort_time_random, bubble_sort_time_sorted]

# Crea un DataFrame con la columna "Category" ordenada por Bubble Sort
unique_categories = eliminate_duplicates(categories)
category_df_bub = pd.DataFrame(unique_categories, columns=["Category"])
category_df_bub.to_csv("ByCategory/Bubble.csv", index=False)

print(f"--------Tiempo de ejecución de Bubble Sort normal: {bubble_sort_time_normal} segundos-----------")
print(f"--------Tiempo de ejecución de Bubble Sort revertido: {bubble_sort_time_reverse} segundos-----------")
print(f"--------Tiempo de ejecución de Bubble Sort aleatorio: {bubble_sort_time_random} segundos-----------")
print(f"--------Tiempo de ejecución de Bubble Sort ordenado: {bubble_sort_time_sorted} segundos-----------")
print()


# Volver a cargar el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Copia la columna "Category" en una lista para ordenarla
categories = df["Category"].astype(str).tolist()

# Lista preordenada
sorted_categories = sorted(categories)

# Lista preordenada de forma revertida
reverse_sorted_categories = sorted(categories, reverse=True)

# Lista preordenada de forma aleatoria
random_categories = random.sample(categories, len(categories))

# Mide el tiempo de ejecución de Quick Sort para la lista preordenada
start_time = time.time()
qck.quick_sort_strings(sorted_categories, 0, len(sorted_categories) - 1)
end_time = time.time()
quick_sort_time_sorted = end_time - start_time

# Mide el tiempo de ejecución de Quick Sort para la lista preordenada de forma revertida
start_time = time.time()
qck.quick_sort_strings(reverse_sorted_categories, 0, len(reverse_sorted_categories) - 1)
end_time = time.time()
quick_sort_time_reverse = end_time - start_time

# Mide el tiempo de ejecución de Quick Sort para la lista preordenada de forma aleatoria
start_time = time.time()
qck.quick_sort_strings(random_categories, 0, len(random_categories) - 1)
end_time = time.time()
quick_sort_time_random = end_time - start_time

# Mide el tiempo de ejecución de Quick Sort para la lista ordenada
start_time = time.time()
qck.quick_sort_strings(categories, 0, len(categories) - 1)
end_time = time.time()
quick_sort_time_normal = end_time - start_time

# Guardar el tiempo de ejecución en la lista
quick_sort_time = [quick_sort_time_normal, quick_sort_time_reverse, quick_sort_time_random, quick_sort_time_sorted]

# Crea un DataFrame con la columna "Category" ordenada por Quick Sort
unique_categories = eliminate_duplicates(categories)
category_df_qck = pd.DataFrame(unique_categories, columns=["Category"])
category_df_qck.to_csv("ByCategory/QuickSort.csv", index=False)

print(f"--------Tiempo de ejecución de Quick Sort normal: {quick_sort_time_normal} segundos-----------")
print(f"--------Tiempo de ejecución de Quick Sort revertido: {quick_sort_time_reverse} segundos-----------")
print(f"--------Tiempo de ejecución de Quick Sort aleatorio: {quick_sort_time_random} segundos-----------")
print(f"--------Tiempo de ejecución de Quick Sort ordenado: {quick_sort_time_sorted} segundos-----------")
print()


# Volver a cargar el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Copia la columna "Category" en una lista para ordenarla
categories = df["Category"].astype(str).tolist()

# Lista preordenada
sorted_categories = sorted(categories)

# Lista preordenada de forma revertida
reverse_sorted_categories = sorted(categories, reverse=True)

# Lista preordenada de forma aleatoria
random_categories = random.sample(categories, len(categories))

# Mide el tiempo de ejecución de Merge Sort para la lista preordenada
start_time = time.time()
mrg.merge_sort(sorted_categories)
end_time = time.time()
merge_sort_time_sorted = end_time - start_time

# Mide el tiempo de ejecución de Merge Sort para la lista preordenada de forma revertida
start_time = time.time()
mrg.merge_sort(reverse_sorted_categories)
end_time = time.time()
merge_sort_time_reverse = end_time - start_time

# Mide el tiempo de ejecución de Merge Sort para la lista preordenada de forma aleatoria
start_time = time.time()
mrg.merge_sort(random_categories)
end_time = time.time()
merge_sort_time_random = end_time - start_time

# Mide el tiempo de ejecución de Merge Sort para la lista ordenada
start_time = time.time()
mrg.merge_sort(categories)
end_time = time.time()
merge_sort_time_normal = end_time - start_time

# Guardar el tiempo de ejecución en la lista
merge_sort_time = [merge_sort_time_normal, merge_sort_time_reverse, merge_sort_time_random, merge_sort_time_sorted]

# Crea un DataFrame con la columna "Category" ordenada por Merge Sort
unique_categories = eliminate_duplicates(categories)
category_df_mrg = pd.DataFrame(unique_categories, columns=["Category"])
category_df_mrg.to_csv("ByCategory/MergeSort.csv", index=False)

print(f"--------Tiempo de ejecución de Merge Sort normal: {merge_sort_time_normal} segundos-----------")
print(f"--------Tiempo de ejecución de Merge Sort revertido: {merge_sort_time_reverse} segundos-----------")
print(f"--------Tiempo de ejecución de Merge Sort aleatorio: {merge_sort_time_random} segundos-----------")
print(f"--------Tiempo de ejecución de Merge Sort ordenado: {merge_sort_time_sorted} segundos-----------")


# Graficar los resultados
labels = ['Normal', 'Revertido', 'Aleatorio', 'Ordenado']
width = 0.2  # Ancho de las barras

fig, ax = plt.subplots(figsize=(10, 6))

bar1 = ax.bar(
    [i - 1.5 * width for i in range(1, 5)],
    insertion_sort_time,
    width,
    label='Insertion Sort',
    align='center',
)

bar2 = ax.bar(
    [i - 0.5 * width for i in range(1, 5)],
    bubble_sort_time,
    width,
    label='Bubble Sort',
    align='center',
)

bar3 = ax.bar(
    [i + 0.5 * width for i in range(1, 5)],
    quick_sort_time,
    width,
    label='Quick Sort',
    align='center',
)

bar4 = ax.bar(
    [i + 1.5 * width for i in range(1, 5)],
    merge_sort_time,
    width,
    label='Merge Sort',
    align='center',
)

ax.set_xlabel('Tipo de Datos')
ax.set_ylabel('Tiempo de Ejecución (segundos)')
ax.set_title('Comparación de Tiempos de Ejecución de Algoritmos de Ordenación por Categoría')
ax.set_xticks([i for i in range(1, 5)])
ax.set_xticklabels(labels)
ax.legend()

plt.show()

