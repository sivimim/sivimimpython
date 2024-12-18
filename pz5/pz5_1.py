#Составить функцию, которая выполнит суммирования числового ряда.

def sum_os(start, end):
    # Проверка, что начальное значение меньше или равно конечному
    if start > end:
        return "Ошибка: начальное значение должно быть меньше или равно конечному."

    total_sum = 0
    for number in range(start, end + 1):
        total_sum += number

    return total_sum

start = int(input("Введите начальное значение: "))
end = int(input("Введите конечное значение: "))

result = sum_os(start, end)
print(f"Сумма чисел от {start} до {end} равна: {result}")
