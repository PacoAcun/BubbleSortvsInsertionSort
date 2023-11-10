import pandas as pd
import time
import matplotlib.pyplot as plt
import InsertionSort as ins
import BubbleSort as bub
import QuickSort as qck
import MergeSort as mrg

df = pd.read_csv("Netflix DB.csv")

# Copia la columna "Name of movie" en una lista para ordenarla
names = df["Name of movie"].tolist()

# Mide el tiempo de ejecución de Insertion Sort
start_time = time.time()
ins.insertion_sort(names)  # Modifica InsertionSort para trabajar con cadenas de texto
end_time = time.time()

# Crea un DataFrame con la columna "Name of movie" ordenada por Insertion Sort
name_df_ins = pd.DataFrame(names, columns=["Name of movie"])
name_df_ins.to_csv("ByName/Insertion.csv", index=False)

print(name_df_ins.head())

print(f"--------Tiempo de ejecución de Insertion Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en una lista
tiempos = [end_time - start_time]


print()
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

print(name_df_bub.head())

print(f"----------Tiempo de ejecución de Bubble Sort: {end_time - start_time} segundos------------")

# Guardar el tiempo de ejecución en la lista
tiempos.append(end_time - start_time)

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

print(name_df_qck.head())

print(f"--------Tiempo de ejecución de Quick Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en la lista
tiempos.append(end_time - start_time)

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

print(name_df_mrg.head())

print(f"--------Tiempo de ejecución de Merge Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en la lista
tiempos.append(end_time - start_time)

# Graficar los tiempos de ejecución
algoritmos = ["Insertion Sort", "Bubble Sort","Quick Sort", "Merge Sort"]
plt.bar(algoritmos, tiempos)
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de Tiempos de Ejecución")
plt.show()