import sys
sys.stdout.reconfigure(encoding='utf-8')
import time


# def f (x):
#     return x + 12
# z = f (4)

# if z == 5:
#     print("z равно 5")
# else:
#     print("Ошибка кода исправьте")

# def f (x, y, z):
#     return x + y + z 
# result = f (22, 11, 33)
# print(result)
# def f ():
#     z = 1 + 1
#     result = f ()
#     print(result)

# stras = "Ivar"
# length = len(stras)
# print(length)

# # Преобразуем строку в float
# x = "3"
# x_float = float(x)

# # Преобразуем float в строку
# y = 3.14
# y_str = str(y)

# # Преобразуем строку в целое число
# z = "42"
# z_int = int(z)

# print(x_float)  # 3.14
# print(y_str)    # "3.14"
# print(z_int)    # 42




# Первая программа
age = input("Укажите возраст: ")

if age.isdigit():
    int_age = int(age)
    if int_age < 21:
        print("Вы - молоды!")
    else:
        print("Ну вы и старик!")
else:
    print("Пожалуйста, введите корректный возраст (число).")

time.sleep(5)  # Пауза 5 секунд

# Вторая программа
n = input("Введите число: ")
n = int(n)

if n % 2 == 0:
    print("n - четное число")
else:
    print("n - не четное число")

time.sleep(5)  # Пауза 5 секунд

# Третья программа (функция)
def even_odd():
    n = input("Введи число: ")
    n = int(n)
    if n % 2 == 0:
        print("Чётное")
    else:
        print("Нечётное")



def f (x = 2):
    return x ** x
print (f())
print(f(12))


def add_it(r, y = 10):
    return r + y
result = add_it (10)
print(result)

# Вызов функции трижды
even_odd()
even_odd()
even_odd()
f()
add_it()
