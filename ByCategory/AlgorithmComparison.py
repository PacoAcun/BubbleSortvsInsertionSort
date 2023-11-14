import pandas as pd
import time
import matplotlib.pyplot as plt
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
categories = df["Category"].tolist()

# Mide el tiempo de ejecución de Insertion Sort
start_time = time.time()
ins.insertion_sort(categories)  # Modifica InsertionSort para trabajar con cadenas de texto
end_time = time.time()

unique_categories = eliminate_duplicates(categories)

# Crea un DataFrame con la columna "Category" ordenada y sin duplicados
category_df_ins = pd.DataFrame(unique_categories, columns=["Category"])
category_df_ins.to_csv("ByCategory/Insertion.csv", index=False)

#print(category_df_ins.head())

print(f"--------Tiempo de ejecución de Insertion Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en una lista
insertion_sort_time = end_time - start_time


print()


# Vuelve a cargar el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Copia la columna "Category" en una lista para ordenarla
Categories = df["Category"].tolist()

# Mide el tiempo de ejecución de Bubble Sort
start_time = time.time()
bub.bubble_sort(Categories)  # Modifica BubbleSort para trabajar con cadenas de texto
end_time = time.time()

unique_categories = eliminate_duplicates(categories)

# Crea un DataFrame con la columna "Category" ordenada por Bubble Sort
category_df_bub = pd.DataFrame(unique_categories, columns=["Category"])
category_df_bub.to_csv("ByCategory/Bubble.csv", index=False)

#print(category_df_bub.head())

print(f"----------Tiempo de ejecución de Bubble Sort: {end_time - start_time} segundos------------")

# Guardar el tiempo de ejecución en la lista
bubble_sort_time = end_time - start_time

print()

# Volver a cargar el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Convertir la columna "Category" a una lista de cadenas de texto
Categories = df["Category"].astype(str).tolist()

# Medir el tiempo de ejecución de Quick Sort
start_time = time.time()
qck.quick_sort_strings(Categories, 0, len(Categories) - 1)
end_time = time.time()

unique_categories = eliminate_duplicates(categories)

# Crear un DataFrame con la columna "Category" ordenada por Quick Sort
category_df_qck = pd.DataFrame(unique_categories, columns=["Category"])
category_df_qck.to_csv("ByCategory/QuickSort.csv", index=False)

#print(category_df_qck.head())

print(f"--------Tiempo de ejecución de Quick Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en la lista
quick_sort_time = end_time - start_time

print()

# Volver a cargar el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Convertir la columna "Category" a una lista de cadenas de texto
Categories = df["Category"].astype(str).tolist()

# Medir el tiempo de ejecución de Quick Sort
start_time = time.time()
mrg.merge_sort(Categories)  # Asegúrate de que QuickSort funcione correctamente
end_time = time.time()

unique_categories = eliminate_duplicates(categories)

# Crear un DataFrame con la columna "Category" ordenada por Quick Sort
category_df_mrg = pd.DataFrame(unique_categories, columns=["Category"])
category_df_mrg.to_csv("ByCategory/Merge.csv", index=False)

#print(category_df_mrg.head())

print(f"--------Tiempo de ejecución de Merge Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en la lista
merge_sort_time = end_time - start_time

# Graficar los tiempos de ejecución
plt.figure(figsize=(10, 5))
plt.bar("Insertion Sort", insertion_sort_time, color="blue", label="Insertion Sort")
plt.bar("Bubble Sort", bubble_sort_time, color="red", label="Bubble Sort")
plt.bar("Quick Sort", quick_sort_time, color="yellow", label="Quick Sort")
plt.bar("Merge Sort", merge_sort_time, color="green", label="Merge Sort")
plt.title("Tiempo de Ejecución de Algoritmos de Ordenación")
plt.xlabel("Algoritmo")
plt.ylabel("Tiempo (segundos)")
plt.legend()
plt.show()