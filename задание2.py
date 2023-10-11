# Первый вектор (строки)
vector1 = ["apple", "banana", "cherry", "date", "fig"]

# Второй вектор (целые числа)
vector2 = [5, 10, 15, 20, 25]
# Длина второго вектора
length = len(vector2)
print("Длина второго вектора:", length)

# Первый элемент второго вектора
first_element = vector2[0]
print("Первый элемент второго вектора:", first_element)

# Элементы со второго по четвёртый
elements_2_to_4 = vector2[1:4]
print("Элементы со второго по четвёртый:", elements_2_to_4)
# Инициализация третьего вектора для сложения
vector3 = [3, 6, 9, 12, 15]

# Сложение второго и третьего векторов
sum_vector = [x + y for x, y in zip(vector2, vector3)]
print("Результат сложения второго и третьего векторов:", sum_vector)
# Расчет среднего значения элементов второго вектора
average = sum(vector2) / len(vector2)
print("Среднее значение элементов второго вектора:", average)
def divide_by_two(vector):
    # Проверка типа элемента перед делением
    result = []
    for x in vector:
        if isinstance(x, int):
            result.append(x / 2)
        else:
            result.append(x)  # Если элемент не является целым числом, оставляем его без изменений
    return result

# Применение функции к первому вектору
result = divide_by_two(vector1)
print("Результат применения функции к первому вектору:", result)

# Первая матрица
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Вторая матрица
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
# Первый столбец (индекс 0)
first_column = [row[0] for row in matrix1]
print("Первый столбец матрицы:", first_column)

# Вторая строка (индекс 1)
second_row = matrix1[1]
print("Вторая строка матрицы:", second_row)
# Элемент на пересечении диагоналей (в данном случае, это элемент с индексом [1][1])
diagonal_intersection = matrix1[1][1]
print("Элемент на пересечении двух диагоналей матрицы:", diagonal_intersection)
