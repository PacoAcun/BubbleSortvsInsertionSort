import pandas as pd
import time
import matplotlib.pyplot as plt
import InsertionSort as ins
import BubbleSort as bub

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

# Graficar los tiempos de ejecución
algoritmos = ["Insertion Sort", "Bubble Sort"]
plt.bar(algoritmos, tiempos)
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de Tiempos de Ejecución")
plt.show()