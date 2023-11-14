import pandas as pd
import time
import matplotlib.pyplot as plt
import BubbleSort as bub
import InsertionSort as ins
import QuickSort as qck
import MergeSort as mrg

def convert_age_rating(age_rating):
    if age_rating in ["ALL", "All"] or pd.isna(age_rating) or age_rating == "" or age_rating == "TV-MA":
        return 0
    elif isinstance(age_rating, str) and age_rating.endswith("+"):
        return int(age_rating.rstrip('+'))
    else:
        return int(age_rating)

df = pd.read_csv("Netflix DB.csv")

print("By age :")
print()


# Copia la columna "Age Rating" en una lista para ordenarla
age_ratings = df["Age Rating"].tolist()

# Convierte la lista de "Age Rating" para que sea ordenable
age_ratings = [convert_age_rating(age_rating) for age_rating in age_ratings]

# Mide el tiempo de ejecución de Insertion Sort
start_time = time.time()
ins.insertion_sort(age_ratings)  # Utiliza el algoritmo de inserción modificado
end_time = time.time()

# Crea un DataFrame con la columna "Age Rating" ordenada por Insertion Sort
age_rating_df_ins = pd.DataFrame(age_ratings, columns=["Age Rating"])
age_rating_df_ins.to_csv("ByAge/Insertion.csv", index=False)

#print(age_rating_df_ins.head())

print(f"--------Tiempo de ejecución de Insertion Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en una lista
insertion_sort_time = end_time - start_time

print()

# Vuelve a cargar el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Copia la columna "Age Rating" en una lista para ordenarla
age_ratings = df["Age Rating"].tolist()

# Convierte la lista de "Age Rating" para que sea ordenable
age_ratings = [convert_age_rating(age_rating) for age_rating in age_ratings]

# Mide el tiempo de ejecución de Bubble Sort
start_time = time.time()
bub.bubble_sort(age_ratings)  # Utiliza el algoritmo de burbuja modificado
end_time = time.time()

# Crea un DataFrame con la columna "Age Rating" ordenada por Bubble Sort
age_rating_df_bub = pd.DataFrame(age_ratings, columns=["Age Rating"])
age_rating_df_bub.to_csv("ByAge/Bubble.csv", index=False)

#print(age_rating_df_bub.head())

print(f"----------Tiempo de ejecución de Bubble Sort: {end_time - start_time} segundos------------")

# Guardar el tiempo de ejecución en la lista
bubble_sort_time = end_time - start_time


print()


# Vuelve a cargar el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Copia la columna "Age Rating" en una lista para ordenarla
age_ratings = df["Age Rating"].tolist()

# Convierte la lista de "Age Rating" para que sea ordenable
age_ratings = [convert_age_rating(age_rating) for age_rating in age_ratings]

# Mide el tiempo de ejecución de Bubble Sort
start_time = time.time()
qck.quick_sort(age_ratings, 0, len(age_ratings) - 1)
end_time = time.time()

# Crea un DataFrame con la columna "Age Rating" ordenada por Bubble Sort
age_rating_df_qck = pd.DataFrame(age_ratings, columns=["Age Rating"])
age_rating_df_qck.to_csv("ByAge/QuickSort.csv", index=False)

#print(age_rating_df_qck.head())

print(f"----------Tiempo de ejecución de Quick Sort: {end_time - start_time} segundos------------")

# Guardar el tiempo de ejecución en la lista
quick_sort_time = end_time - start_time


print()


# Vuelve a cargar el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Copia la columna "Age Rating" en una lista para ordenarla
age_ratings = df["Age Rating"].tolist()

# Convierte la lista de "Age Rating" para que sea ordenable
age_ratings = [convert_age_rating(age_rating) for age_rating in age_ratings]

# Mide el tiempo de ejecución de Bubble Sort
start_time = time.time()
mrg.merge_sort(age_ratings)
end_time = time.time()

# Crea un DataFrame con la columna "Age Rating" ordenada por Bubble Sort
age_rating_df_mrg = pd.DataFrame(age_ratings, columns=["Age Rating"])
age_rating_df_mrg.to_csv("ByAge/MergeSort.csv", index=False)

#print(age_rating_df_mrg.head())

print(f"----------Tiempo de ejecución de Merge Sort: {end_time - start_time} segundos------------")

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