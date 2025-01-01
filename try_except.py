import sys
sys.stdout.reconfigure(encoding='utf-8')
import time



a = input("Введите число: ")
b = input("Введите число: ")


a = int(a)
b = int(b)
try:
    print(a / b )
except (ZeroDivisionError, ValueError):
    print("Ошибка ввода")