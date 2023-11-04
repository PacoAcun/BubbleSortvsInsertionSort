import pandas as pd #pip install pandas
import time
import matplotlib.pyplot as plt #pip install matplotlib
import InsertionSort as ins
import BubbleSort as bub

df = pd.read_csv("Netflix DB.csv")

# Copia la columna "Year" en una lista para ordenarla
year = df["Year"].tolist()

# Mide el tiempo de ejecución de Insertion Sort
start_time = time.time()
ins.insertion_sort(year)
end_time = time.time()

# Crea un DataFrame con la columna "Year" ordenada por Insertion Sort
year_df_ins = pd.DataFrame(year, columns=["Year"])
year_df_ins.to_csv("ByYear/Insertion.csv", index=False)

print(year_df_ins.head())

print(f"--------Tiempo de ejecución de Insertion Sort: {end_time - start_time} segundos-----------")

# Guardar el tiempo de ejecución en una lista
tiempos = [end_time - start_time]


print()
print()


# Vuelve a cargar el DataFrame original
df = pd.read_csv("Netflix DB.csv")

# Copia la columna "Year" en una lista para ordenarla
year = df["Year"].tolist()

# Mide el tiempo de ejecución de Bubble Sort
start_time = time.time()
bub.bubble_sort(year)
end_time = time.time()

# Crea un DataFrame con la columna "Year" ordenada por Bubble Sort
year_df_bub = pd.DataFrame(year, columns=["Year"])
year_df_bub.to_csv("ByYear/Bubble.csv", index=False)

print(year_df_bub.head())

print(f"----------Tiempo de ejecución de Bubble Sort: {end_time - start_time} segundos------------")

# Guardar el tiempo de ejecución en la lista
tiempos.append(end_time - start_time)


# Graficar los tiempos de ejecución
algoritmos = ["Insertion Sort", "Bubble Sort"]
plt.bar(algoritmos, tiempos)
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de Tiempos de Ejecución")
plt.show()