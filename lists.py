import sys
sys.stdout.reconfigure(encoding='utf-8')
import time

#Списки
phone = ["Samsung", "Vivo", "Xiomi", "LG", "Oppo"]
phone.append("Nokia")
phone.append("Meizu")
# print(phone)
print(phone[1])



colors = ["red", "black", "orange"]
# Вывожу все цвета
print(colors)
# Меняю индекс red на pink
colors  [0] = "pink"
# Удаляю последний цвет в списке
item = colors.pop()
print(colors)
colors2 = ["white", "blue", "yello"]
# Добавляю цвет к списку
colors2.append("grey")
all_colors = colors + colors2
# Поиск цвета в списке
print("grey" in all_colors)
print(all_colors)


fruits = ["apple", "banana", "melon", "watermelon"]
quess = input("Угадай фрукт:")
# Приводим как ввод пользователя, так и элементы списка к нижнему регистру для сравнения
if quess.lower() in [fruits.lower() for fruits in fruits]:
    print("Вы угадали!")
else:
    print("Не правильно! Попробуйте еще раз!")



#Кортежи

person_data = ("Iskanderov Ivar", 2004, True)
print(int("2004") in person_data)
print(person_data)


#Словарь


person = {
    "name": "Ivar",
    "age": 19,
    "city": "Moscow",
    "Is_student": True
}
person ["age"] = 21
del person["Is_student"]
print(person)



anime = {
    "1":"Naruto",
    "2": "Bleach",
    "3": "Chainsaw Man",
    "4": "Bakugan"
}
watch = input("Введите код:")
if watch in anime:
    anime = anime[watch]
    print(anime)
else:
    print("Не найдено в списке!")