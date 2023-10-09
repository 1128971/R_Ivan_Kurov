# Инициализация переменных
integer_variable = 42  # Любое целое число
float_variable = 3.14  # Любое число с плавающей точкой
string_variable = "Привет, мир!"  # Любая строка

# Вывод результата деления первой переменной на вторую
result = round(integer_variable / float_variable, 2)
print(f"Результат деления: {result}")

# Вывод результата сравнения первой переменной со второй
comparison_result = integer_variable > float_variable
print(f"Сравнение: {comparison_result}")

# Вывод третьей переменной три раза подряд через запятую
print(f"Третья переменная: {string_variable}, {string_variable}, {string_variable}")

# Используем цикл для вывода фразы с 2021 по 2023 год
for year in range(2021, 2024):
    print(f"Маркетинговый проект запустился в {year} году")

# Используем цикл и условный оператор для вывода фразы с 2024 по 2030 год
for year in range(2024, 2031):
    if year == 2024:
        print(f"Маркетинговый проект только запуститься в {year} году")
    else:
        print(f"Маркетинговый проект запустился в {year} году")
