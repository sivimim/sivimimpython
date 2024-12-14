def day_of_week(k):
    # Номер дня недели для 1 января (четверг)
    starting_day = 4  # 4 - четверг
    # Вычисляем номер дня недели для K-го дня
    day_of_week_number = (starting_day + (k - 1)) % 7
    return day_of_week_number

# Пример использования
K = int(input("Введите номер дня от 1 до 365: "))
if 1 <= K <= 365:
    result = day_of_week(K)
    print(f"Номер дня недели для {K}-го дня года: {result}")
else:
    print("Пожалуйста, введите число в диапазоне от 1 до 365.")
