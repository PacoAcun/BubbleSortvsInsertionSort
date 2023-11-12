import pandas as pd
import time
import matplotlib.pyplot as plt
import InsertionSort as ins
import BubbleSort as bub
import QuickSort as qck
import MergeSort as mrg

# Carga el DataFrame original
df = pd.read_csv("Netflix DB.csv")
print(df.head())

print()
print()

# Reemplaza los campos vacíos con '0h 0m' y convierte la columna "Duration" a formato de tiempo
df["Duration"] = df["Duration"].fillna('0h 0m')

# Copia la columna "Duration" en una lista para ordenarla
duration = df["Duration"].tolist()

def extract_seasons(duration):
    duration = [element for element in duration if "1 Season" not in element and "Season 1" not in element]
    return duration

def to_minutes(duration):
    if 'Season' in duration:
        return float('inf')  # Representing 'Season' as infinite minutes
    else:
        # Split the duration string into components
        components = duration.replace('h', ' ').replace('m', ' ').split()
        
        # Check if there are enough components to unpack
        if len(components) >= 2:
            hours, minutes = map(int, components[:2])
            return hours * 60 + minutes
        else:
            return 0  # Default case for unexpected formats

duration_without_seasons = extract_seasons(duration)
duration_clean = [to_minutes(item) for item in duration_without_seasons]

# Mide el tiempo de ejecución de Insertion Sort
start_time = time.time()
sorted_duration = ins.insertion_sort(duration_clean)
end_time = time.time()

# Crea un DataFrame con la columna "Duration" ordenada por Insertion Sort
sorted_duration_df_ins = pd.DataFrame(sorted_duration, columns=["Duration"])
sorted_duration_df_ins.to_csv("ByDuration/Insertion.csv", index=False)

print(sorted_duration_df_ins.head())

print(f"--------Tiempo de ejecución de Insertion Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en una lista
insertion_sort_time = end_time - start_time


print()
print()


# Carga el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Reemplaza los campos vacíos con '0h 0m' y convierte la columna "Duration" a formato de tiempo
df["Duration"] = df["Duration"].fillna('0h 0m')

# Copia la columna "Duration" en una lista para ordenarla
duration = df["Duration"].tolist()

duration_without_seasons = extract_seasons(duration)
duration_clean = [to_minutes(item) for item in duration_without_seasons]

# Mide el tiempo de ejecución de Bubble Sort
start_time = time.time()
bub.bubble_sort(duration_clean)
end_time = time.time()

# Crea un DataFrame con la columna "Duration" ordenada por Bubble Sort
sorted_duration_df_bub = pd.DataFrame(duration_clean, columns=["Duration"])
sorted_duration_df_bub.to_csv("ByDuration/Bubble.csv", index=False)

print(sorted_duration_df_bub.head())

print(f"--------Tiempo de ejecución de Bubble Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en una lista
bubble_sort_time = end_time - start_time

print()
print()

# Carga el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Reemplaza los campos vacíos con '0h 0m' y convierte la columna "Duration" a formato de tiempo
df["Duration"] = df["Duration"].fillna('0h 0m')

# Copia la columna "Duration" en una lista para ordenarla
duration = df["Duration"].tolist()

duration_without_seasons = extract_seasons(duration)
duration_clean = [to_minutes(item) for item in duration_without_seasons]

# Mide el tiempo de ejecución de Quick Sort
start_time = time.time()
qck.quick_sort(duration_clean)
end_time = time.time()

# Crea un DataFrame con la columna "Duration" ordenada por Quick Sort
sorted_duration_df_qck = pd.DataFrame(duration_clean, columns=["Duration"])
sorted_duration_df_qck.to_csv("ByDuration/QuickSort.csv", index=False)

print(sorted_duration_df_qck.head())

print(f"--------Tiempo de ejecución de Quick Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en una lista
quick_sort_time = end_time - start_time

print()
print()

# Carga el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Reemplaza los campos vacíos con '0h 0m' y convierte la columna "Duration" a formato de tiempo
df["Duration"] = df["Duration"].fillna('0h 0m')

# Copia la columna "Duration" en una lista para ordenarla
duration = df["Duration"].tolist()

duration_without_seasons = extract_seasons(duration)
duration_clean = [to_minutes(item) for item in duration_without_seasons]

# Mide el tiempo de ejecución de Merge Sort
start_time = time.time()
mrg.merge_sort(duration_clean)
end_time = time.time()

# Crea un DataFrame con la columna "Duration" ordenada por Merge Sort
sorted_duration_df_mrg = pd.DataFrame(duration_clean, columns=["Duration"])
sorted_duration_df_mrg.to_csv("ByDuration/MergeSort.csv", index=False)

print(sorted_duration_df_mrg.head())

print(f"--------Tiempo de ejecución de Merge Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en una lista
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
