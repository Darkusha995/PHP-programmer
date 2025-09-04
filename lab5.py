# 1. Дан произвольный список. Представьте его в обратном порядке.
numbers = [10, 20, 30, 40, 50]
print("Оригинал:", numbers)
print("Обратный порядок:", numbers[::-1])


# 2. Функция list_sort(lst), сортирует список по убыванию абсолютного значения
def list_sort(lst):
    return sorted(lst, key=lambda x: abs(x), reverse=True)

example = [3, -15, 7, -2, 20]
print("До сортировки:", example)
print("После сортировки:", list_sort(example))


# 3. Функция change(lst), меняет местами первый и последний элемент
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

items = ["первый", "середина", "последний"]
print("До:", items)
print("После:", change(items))