import pandas as pd
import time
import matplotlib.pyplot as plt
import random
import InsertionSort as ins
import BubbleSort as bub
import QuickSort as qck
import MergeSort as mrg

insertion_times = []
bubble_times = []
quick_times = []
merge_times = []

df = pd.read_csv("Netflix DB.csv")

print("By duration :")
print()


df["Duration"] = df["Duration"].fillna('0h 0m')


duration = df["Duration"].tolist()

def extract_seasons(duration):
    duration = [element for element in duration if "1 Season" not in element and "Season 1" not in element]
    return duration

def to_minutes(duration):
    if 'Season' in duration:
        return float('inf')
    else:
        components = duration.replace('h', ' ').replace('m', ' ').split()
        
        if len(components) >= 2:
            hours, minutes = map(int, components[:2])
            return hours * 60 + minutes
        else:
            return 0 

duration_without_seasons = extract_seasons(duration)
duration_clean = [to_minutes(item) for item in duration_without_seasons]


sorted_duration = sorted(duration_clean)

reverse_sorted_duration = sorted(duration_clean, reverse=True)

random_duration = random.sample(duration_clean, len(duration_clean))


start_time = time.time()
ins.insertion_sort(sorted_duration)
end_time = time.time()
insertion_sort_time_sorted = end_time - start_time
insertion_times.append(insertion_sort_time_sorted)

start_time = time.time()
ins.insertion_sort(reverse_sorted_duration)
end_time = time.time()
insertion_sort_time_reverse = end_time - start_time
insertion_times.append(insertion_sort_time_reverse)

start_time = time.time()
ins.insertion_sort(random_duration)
end_time = time.time()
insertion_sort_time_random = end_time - start_time
insertion_times.append(insertion_sort_time_random)

start_time = time.time()
ins.insertion_sort(duration_clean)
end_time = time.time()
insertion_sort_time_normal = end_time - start_time
insertion_times.append(insertion_sort_time_normal)

sorted_duration_df_ins = pd.DataFrame(sorted_duration, columns=["Duration"])
sorted_duration_df_ins.to_csv("ByDuration/Insertion.csv", index=False)

print(f"--------Tiempo de ejecución de Insertion Sort normal: {insertion_sort_time_normal} segundos-----------")
print(f"--------Tiempo de ejecución de Insertion Sort revertido: {insertion_sort_time_reverse} segundos-----------")
print(f"--------Tiempo de ejecución de Insertion Sort aleatorio: {insertion_sort_time_random} segundos-----------")
print(f"--------Tiempo de ejecución de Insertion Sort ordenado: {insertion_sort_time_sorted} segundos-----------")


print()


df = pd.read_csv("Netflix DB.csv")


df["Duration"] = df["Duration"].fillna('0h 0m')

duration = df["Duration"].tolist()

duration_without_seasons = extract_seasons(duration)
duration_clean = [to_minutes(item) for item in duration_without_seasons]


sorted_duration = sorted(duration_clean)

reverse_sorted_duration = sorted(duration_clean, reverse=True)

random_duration = random.sample(duration_clean, len(duration_clean))


start_time = time.time()
bub.bubble_sort(sorted_duration)
end_time = time.time()
bubble_sort_time_sorted = end_time - start_time
bubble_times.append(bubble_sort_time_sorted)

start_time = time.time()
bub.bubble_sort(reverse_sorted_duration)
end_time = time.time()
bubble_sort_time_reverse = end_time - start_time
bubble_times.append(bubble_sort_time_reverse)

start_time = time.time()
bub.bubble_sort(random_duration)
end_time = time.time()
bubble_sort_time_random = end_time - start_time
bubble_times.append(bubble_sort_time_random)

start_time = time.time()
bub.bubble_sort(duration_clean)
end_time = time.time()
bubble_sort_time_normal = end_time - start_time
bubble_times.append(bubble_sort_time_normal)

sorted_duration_df_bub = pd.DataFrame(duration_clean, columns=["Duration"])
sorted_duration_df_bub.to_csv("ByDuration/Bubble.csv", index=False)

print(f"--------Tiempo de ejecución de Bubble Sort normal: {bubble_sort_time_normal} segundos-----------")
print(f"--------Tiempo de ejecución de Bubble Sort revertido: {bubble_sort_time_reverse} segundos-----------")
print(f"--------Tiempo de ejecución de Bubble Sort aleatorio: {bubble_sort_time_random} segundos-----------")
print(f"--------Tiempo de ejecución de Bubble Sort ordenado: {bubble_sort_time_sorted} segundos-----------")


print()


df = pd.read_csv("Netflix DB.csv")


df["Duration"] = df["Duration"].fillna('0h 0m')

duration = df["Duration"].tolist()

duration_without_seasons = extract_seasons(duration)
duration_clean = [to_minutes(item) for item in duration_without_seasons]


sorted_duration = sorted(duration_clean)

reverse_sorted_duration = sorted(duration_clean, reverse=True)

random_duration = random.sample(duration_clean, len(duration_clean))

start_time = time.time()
qck.quick_sort(sorted_duration)
end_time = time.time()
quick_sort_time_sorted = end_time - start_time
quick_times.append(quick_sort_time_sorted)

start_time = time.time()
qck.quick_sort(reverse_sorted_duration)
end_time = time.time()
quick_sort_time_reverse = end_time - start_time
quick_times.append(quick_sort_time_reverse)

start_time = time.time()
qck.quick_sort(random_duration)
end_time = time.time()
quick_sort_time_random = end_time - start_time
quick_times.append(quick_sort_time_random)

start_time = time.time()
qck.quick_sort(duration_clean)
end_time = time.time()
quick_sort_time_normal = end_time - start_time
quick_times.append(quick_sort_time_normal)

sorted_duration_df_qck = pd.DataFrame(duration_clean, columns=["Duration"])
sorted_duration_df_qck.to_csv("ByDuration/QuickSort.csv", index=False)

print(f"--------Tiempo de ejecución de Quick Sort normal: {quick_sort_time_normal} segundos-----------")
print(f"--------Tiempo de ejecución de Quick Sort revertido: {quick_sort_time_reverse} segundos-----------")
print(f"--------Tiempo de ejecución de Quick Sort aleatorio: {quick_sort_time_random} segundos-----------")
print(f"--------Tiempo de ejecución de Quick Sort ordenado: {quick_sort_time_sorted} segundos-----------")


print()


df = pd.read_csv("Netflix DB.csv")


df["Duration"] = df["Duration"].fillna('0h 0m')

duration = df["Duration"].tolist()

duration_without_seasons = extract_seasons(duration)
duration_clean = [to_minutes(item) for item in duration_without_seasons]


sorted_duration = sorted(duration_clean)

reverse_sorted_duration = sorted(duration_clean, reverse=True)

random_duration = random.sample(duration_clean, len(duration_clean))

start_time = time.time()
mrg.merge_sort(sorted_duration)
end_time = time.time()
merge_sort_time_sorted = end_time - start_time
merge_times.append(merge_sort_time_sorted)

start_time = time.time()
mrg.merge_sort(reverse_sorted_duration)
end_time = time.time()
merge_sort_time_reverse = end_time - start_time
merge_times.append(merge_sort_time_reverse)

start_time = time.time()
mrg.merge_sort(random_duration)
end_time = time.time()
merge_sort_time_random = end_time - start_time
merge_times.append(merge_sort_time_random)

start_time = time.time()
mrg.merge_sort(duration_clean)
end_time = time.time()
merge_sort_time_normal = end_time - start_time
merge_times.append(merge_sort_time_normal)

sorted_duration_df_mrg = pd.DataFrame(duration_clean, columns=["Duration"])
sorted_duration_df_mrg.to_csv("ByDuration/MergeSort.csv", index=False)

print(f"--------Tiempo de ejecución de Merge Sort normal: {merge_sort_time_normal} segundos-----------")
print(f"--------Tiempo de ejecución de Merge Sort revertido: {merge_sort_time_reverse} segundos-----------")
print(f"--------Tiempo de ejecución de Merge Sort aleatorio: {merge_sort_time_random} segundos-----------")
print(f"--------Tiempo de ejecución de Merge Sort ordenado: {merge_sort_time_sorted} segundos-----------")

# Graficar los resultados
labels = ['Normal', 'Revertido', 'Aleatorio', 'Ordenado']
width = 0.2 

fig, ax = plt.subplots(figsize=(10, 6))

bar1 = ax.bar(
    [i - 1.5 * width for i in range(1, 5)],
    insertion_times,
    width,
    label='Insertion Sort',
    align='center',
)

bar2 = ax.bar(
    [i - 0.5 * width for i in range(1, 5)],
    bubble_times,
    width,
    label='Bubble Sort',
    align='center',
)

bar3 = ax.bar(
    [i + 0.5 * width for i in range(1, 5)],
    quick_times,
    width,
    label='Quick Sort',
    align='center',
)

bar4 = ax.bar(
    [i + 1.5 * width for i in range(1, 5)],
    merge_times,
    width,
    label='Merge Sort',
    align='center',
)

ax.set_xlabel('Tipo de Datos')
ax.set_ylabel('Tiempo de Ejecución (segundos)')
ax.set_title('Comparación de Tiempos de Ejecución de Algoritmos de Ordenación')
ax.set_xticks([i for i in range(1, 5)])
ax.set_xticklabels(labels)
ax.legend()

plt.show()

