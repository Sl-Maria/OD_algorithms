# sorting algorithms

list = [5, 2, 4, 6, 1, 3, 9, 7, 8, 0]

# Bubble sort
mas = list
n = len(mas)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if mas[j] > mas[j + 1]:
            mas[j], mas[j + 1] = mas[j + 1], mas[j]
print("Bubble sort:", mas)

# quick sort
def quick_sort(mas):
    if len(mas) <= 1:
        return mas
    else:
        rock = mas[0]
        less = [i for i in mas[1:] if i <= rock]
        great = [i for i in mas[1:] if i > rock]
        return quick_sort(less) + [rock] + quick_sort(great)
mas = list
print('Quick sort:', quick_sort(mas))

# Selection sort
def selection_sort(mas):
    for i in range(len(mas)):
        min_index = i
        for j in range(i + 1, len(mas)):
            if mas[j] < mas[min_index]:
                min_index = j
        mas[i], mas[min_index] = mas[min_index], mas[i]
    return mas

mas = list
print('Selection sort:', selection_sort(mas))

# Insertion sort
def insertion_sort(mas):
    for i in range(1, len(mas)):
        key = mas[i]
        j = i - 1
        while j >= 0 and mas[j] > key:
            mas[j + 1] = mas[j]
            j -= 1
        mas[j + 1] = key
    return mas
mas = list
print('Insertion sort:', insertion_sort(mas))