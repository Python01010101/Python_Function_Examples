import sys
sys.stdout.reconfigure(encoding='utf-8')
import array
# Cписок товаров
online_shop = ['Phone', 'Laptop', 'Watch', 'Tablet']


# Добавление товара .append
online_shop.append('TV')


# Удаление товара .remove
online_shop.remove('Watch')


# Разложение товара по алфавиту  Используйте функцию sorted(), которая возвращает новый отсортированный список.
# Метод sort():
#Этот метод изменяет исходный список, упорядочивая элементы в алфавитном порядке.
sorted_shop = sorted(online_shop)
print(online_shop)
# Вывод товара по индексу
print(online_shop [3])
print(sorted_shop)




students = ['Иван', 'Мария', 'Алексей', 'Дарья']

# Разложение студентов по алфавитному порядку
sorted_students = sorted(students)
print("Сортированный список:", sorted_students)

# Вычисляем середину списка
middle_index = len(students) // 2

# Разделяем список на две половины
first_half = students[:middle_index]
second_half = students[middle_index:]

print("Первая половина:", first_half)
print("Вторая половина:", second_half)

# Добавление студента
students.append('Анна')

# Проверка списка на наличие студента "Анна"
for s in students:  # Изменил имя переменной цикла
    if s == 'Анна':
        print("Студент найден!")
        break
else:
    print("Студента с именем 'Анна' нет.")

print("Обновленный список студентов:", students)


# Создаем словарь сотрудника
employee = {
"name": "Ивар Искандеров",
"position": "Разработчик",
"salary": 120000,
"departament": "IT"
}

# Вывод зп сотрудника 
print(f"Зарплата сотрудника: {employee['salary']} рублей")

# Изменение должности на "Старший разработчик"
employee = {'position': 'Разработчик'} 
employee['position'] = 'Старший Python разработчик'


# Добавление нового ключа "years_at_company" со значением 5
employee['years_at_company'] = 5

# Вывод обновленного словаря
print("Обнавленная информация о сотруднике:", employee)