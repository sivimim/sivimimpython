num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
num4 = int(input("Введите четвёртое число: "))

if num1 == num2 == num3:
  different_ordinal = 4
elif num1 == num2 == num4:
  different_ordinal = 3
elif num1 == num3 == num4:
  different_ordinal = 2
else:
  different_ordinal = 1

print(f"Порядковый номер числа отличающийся от остальных: {different_ordinal}")