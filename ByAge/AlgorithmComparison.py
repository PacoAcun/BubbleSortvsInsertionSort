import pandas as pd
import time
import matplotlib.pyplot as plt
import BubbleSort as bub
import InsertionSort as ins

def convert_age_rating(age_rating):
    if age_rating == "ALL" or pd.isna(age_rating) or age_rating == "":
        return "0"  # Asigna un valor representativo para "ALL" o valores vacíos
    if isinstance(age_rating, str) and age_rating.endswith("+"):
        return age_rating.rstrip('+')  # Elimina el símbolo '+' de "X+"
    return str(age_rating)  # Convierte valores numéricos a cadenas de texto


df = pd.read_csv("Netflix DB.csv")

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

print(age_rating_df_ins.head())

print(f"--------Tiempo de ejecución de Insertion Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en una lista
tiempos = [end_time - start_time]

print()
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

print(age_rating_df_bub.head())

print(f"----------Tiempo de ejecución de Bubble Sort: {end_time - start_time} segundos------------")

# Guardar el tiempo de ejecución en la lista
tiempos.append(end_time - start_time)

# Graficar los tiempos de ejecución
algoritmos = ["Insertion Sort", "Bubble Sort"]
plt.bar(algoritmos, tiempos)
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de Tiempos de Ejecución")
plt.show()
