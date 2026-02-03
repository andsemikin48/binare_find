"""Бинарный поиск
Путь: деление отсортированного списка пополам,
если элемент в середине больше или меньше искомого,
то рекурсивно повторяю поиск, сохраняя при этом индекс изначального массива.
При отсутствии элемента вернуть -1.
При значении больше длины массива поднимаю ошибку.
Обработать ошибку ввода или некорректного значения.
"""
import time
"""
from random import randint
arr = [randint(0,1000) for i in range(1000)]
arr_sort = sorted(arr)
print(arr_sort)
"""
#Массив для теста в 10000 элементов
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
    def bin_find(arr, key):
        try:
            key = int(key) if key.isdigit() else -1
            if key == -1:
                raise ValueError
            if key > arr[-1]:
                raise IndexError
            index = 0
            for i in arr:
                if i == key:
                    return index
                else:
                    index += 1
            print("Элемент не найден")
            return -1
        except IndexError:
            print("Значение выходит за пределы массива")
            return -1
        except ValueError:
            print("Некорректное значение")
            return -1
    return bin_find(arr, key)
key_find = input("Введите число для поиска: ")
print(bin_find_wrapper(arr_sort,key_find))
"""Запись примеров в файл
with open('README.md', 'a', encoding='utf-8') as file:
    result = bin_find_wrapper(arr_sort,key_find)
    file.write(f"    Результат: {key_find} {result}\n")
"""