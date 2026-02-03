"""Бинарный поиск
Путь: деление отсортированного списка пополам,
если элемент в середине больше или меньше искомого,
то рекурсивно повторяю поиск, сохраняя при этом индекс изначального массива.
При отсутствии элемента вернуть -1.
При значении больше длины массива поднимаю ошибку.
Обработать ошибку ввода или некорректного значения.
"""
#from random import randint
import time
#arr = [randint(0,1000) for i in range(10000)]
#arr_sort = sorted(arr)
#print(arr_sort)
arr_sort = [i for i in range(10000)]

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_run = f"Время выполнения: {(end - start)*1000:.3f} мс"
        return result, time_run
    return wrapper

@timeit
def bin_find_wrapper(arr, key):
    def bin_find(arr, key, start_index=0):
        try:
            if not arr:
                return -1
            index = len(arr)//2
            value = arr[index]
            if type(key) != int:
                key = int(key) if key.isdigit() else -1
                if key == -1:
                    raise ValueError
            if key < arr[0] or key > arr[-1]:
                return -1
            if key > arr[-1] and len(arr) == 1 and key != value:
                print("Элемент не найден")
                return -1
            elif key == value:
                return start_index + index
            elif key > value:
                find_index = bin_find(arr[index+1:],key, start_index + index +1)
                return find_index
            elif key < value:
                return bin_find(arr[:index],key, start_index)

        except ValueError:
            print("Некорректное значение")
            return -1
    return bin_find(arr, key)

key_find = input("Введите число для поиска: ")
print(bin_find_wrapper(arr_sort,key_find))
"""Запись примеров в файл
with open('README.md', 'a', encoding='utf-8') as file:
    out = bin_find_wrapper(arr_sort,key_find)

    print(out)
    file.write(f"    Результат: {key_find} {out}\n")
"""