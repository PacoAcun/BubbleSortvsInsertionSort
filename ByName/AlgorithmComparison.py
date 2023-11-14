import pandas as pd
import time
import matplotlib.pyplot as plt
import InsertionSort as ins
import BubbleSort as bub
import QuickSort as qck
import MergeSort as mrg

df = pd.read_csv("Netflix DB.csv")

print("By name :")
print()

# Copia la columna "Name of movie" en una lista para ordenarla
names = df["Name of movie"].tolist()

# Mide el tiempo de ejecución de Insertion Sort
start_time = time.time()
ins.insertion_sort(names)  # Modifica InsertionSort para trabajar con cadenas de texto
end_time = time.time()

# Crea un DataFrame con la columna "Name of movie" ordenada por Insertion Sort
name_df_ins = pd.DataFrame(names, columns=["Name of movie"])
name_df_ins.to_csv("ByName/Insertion.csv", index=False)

#print(name_df_ins.head())

print(f"--------Tiempo de ejecución de Insertion Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en una lista
insertion_sort_time = end_time - start_time


print()


# Vuelve a cargar el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Copia la columna "Name of movie" en una lista para ordenarla
names = df["Name of movie"].tolist()

# Mide el tiempo de ejecución de Bubble Sort
start_time = time.time()
bub.bubble_sort(names)  # Modifica BubbleSort para trabajar con cadenas de texto
end_time = time.time()

# Crea un DataFrame con la columna "Name of movie" ordenada por Bubble Sort
name_df_bub = pd.DataFrame(names, columns=["Name of movie"])
name_df_bub.to_csv("ByName/Bubble.csv", index=False)

#print(name_df_bub.head())

print(f"----------Tiempo de ejecución de Bubble Sort: {end_time - start_time} segundos------------")

# Guardar el tiempo de ejecución en la lista
bubble_sort_time = end_time - start_time


print()


# Volver a cargar el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Convertir la columna "Name of movie" a una lista de cadenas de texto
names = df["Name of movie"].astype(str).tolist()

# Medir el tiempo de ejecución de Quick Sort
start_time = time.time()
qck.quick_sort_strings(names, 0, len(names) - 1)
end_time = time.time()

# Crear un DataFrame con la columna "Name of movie" ordenada por Quick Sort
name_df_qck = pd.DataFrame(names, columns=["Name of movie"])
name_df_qck.to_csv("ByName/QuickSort.csv", index=False)

#print(name_df_qck.head())

print(f"--------Tiempo de ejecución de Quick Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en la lista
quick_sort_time = end_time - start_time


print()


# Volver a cargar el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Convertir la columna "Name of movie" a una lista de cadenas de texto
names = df["Name of movie"].astype(str).tolist()

# Medir el tiempo de ejecución de Quick Sort
start_time = time.time()
mrg.merge_sort(names)  # Asegúrate de que QuickSort funcione correctamente
end_time = time.time()

# Crear un DataFrame con la columna "Name of movie" ordenada por Quick Sort
name_df_mrg = pd.DataFrame(names, columns=["Name of movie"])
name_df_mrg.to_csv("ByName/Merge.csv", index=False)

#print(name_df_mrg.head())

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