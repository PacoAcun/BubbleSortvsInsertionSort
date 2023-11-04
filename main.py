import InsertionSort as ins
import BubbleSort as bub
import pandas as pd #pip install pandas
import time

df = pd.read_csv("Netflix DB.csv")

# Copia la columna "Year" en una lista para ordenarla
year = df["Year"].tolist()

# Mide el tiempo de ejecución de Insertion Sort
start_time = time.time()
ins.insertion_sort(year)
end_time = time.time()

# Crea un DataFrame con la columna "Year" ordenada por Insertion Sort
year_df_ins = pd.DataFrame(year, columns=["Year"])
year_df_ins.to_csv("Sort_Year_Ins.csv", index=False)

print(year_df_ins.head())

print(f"--------Tiempo de ejecución de Insertion Sort: {end_time - start_time} segundos-----------")


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
year_df_bub.to_csv("Sort_Year_Bub.csv", index=False)

print(year_df_bub.head())

print(f"----------Tiempo de ejecución de Bubble Sort: {end_time - start_time} segundos------------")
