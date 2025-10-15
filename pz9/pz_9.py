«Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать информацию из строки в словарь, найти среднее арифметическое оценок, результаты вывести на экран»

string_to_convert = 'Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4'

def write_string_in_dict(string: str):
    splited_string = string.split()

    student = " ".join(splited_string[:2]) # студент = срезу до 2 слово разделенной строки
    group = splited_string[2] # группа = 2 слову разделенной строки

    # список оценки = через цикл for каждый элемент(grade) из списка среза слов
    # от 3 до последнего конвертируется в тип инт и записывается в список grades
    grades = [int(grade) for grade in splited_string[3:]]

    return {"ФИ Студента": student, "Группа": group, "Оценки": grades} # возвращаем исходные значения для инициализации словаря


student_dict = write_string_in_dict(string_to_convert) # инициализация словаря

print(student_dict)

grades_link = student_dict["Оценки"] # ссылка на ключ "Оценки"
print("Итоговая оценка:", sum(grades_link) / len(grades_link)) # итоговая оценка = сумма всех оценнок из списка ключа / кол-во элементов списка оценок
