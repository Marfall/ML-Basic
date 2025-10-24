s1 = "Математика Иванов  5"
s2 = "Математика Иванов  4"
s3 = "Литература Иванов  3"
s4 = "Математика Петров  5"
s5 = "Литература Сидоров 3"
s6 = "Литература Петров  5"
s7 = "Литература Иванов  4"
s8 = "Математика Сидоров 3"
s9 = "Математика Петров  5"

# Создаем словарь для хранения данных
data = {}

# Ввод данных
while True:
    # Получаем строку ввода
    # line = input()
    line = "Математика Иванов 5"

    # Проверяем условие выхода
    if line == "":
        break

    # Разбиваем строку на компоненты
    subject, surname, grade = line.split()
    print(subject)

    # Добавляем данные в словарь
    if subject not in data:
        data[subject] = {}
    if surname not in data[subject]:
        data[subject][surname] = data[subject][surname].append(grade)

# Вывод результатов
for subject, students in data.items():
    print(f"\nПредмет: {subject}")
    print("-" * 20)
    print(f"{'Фамилия':<20}{'Оценки':<10}")
    print("-" * 20)

    for surname, grades in students.items():
        # Форматируем список оценок в строку
        grades_str = ", ".join(grades)
        print(f"{surname:<20}{grades_str:<10}")