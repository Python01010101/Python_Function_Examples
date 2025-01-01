import sys
sys.stdout.reconfigure(encoding='utf-8')
import time

def square_number(number):
       """
    Функция принимает число, возводит его в квадрат и возвращает результат.
    
    :param number: Число, которое нужно возвести в квадрат.
    :return: Квадрат числа.
    """
       # Возведение числа в квадрат
       result = number ** 2

        # Возвращаем результат
       return result
input_num = int(input("Введите число: "))
output = square_number(input_num)
print(f"Квадрат числа {input_num} равен {output}")





def return_string(input_string):
    """
    Функция принимает строку в качестве параметра и возвращает её.
    
    :param input_string: Входная строка.
    :return: Та же строка, что была передана.
    """
    return input_string

# Пример использования функции
user_input = input("Введите строку: ")
output1 = return_string(user_input)
print(f"Вы ввели: {output1}")


def combine_string(str1, str2, str3, str4 = "Hi world", str5 = "Ivar"):
      if not str1 or not str2 or not str3:
            raise ValueError("Первые 3 строки не обязательны!")
      result = str1 + "" + str2 + "" + str3 + "" + str4 + "" + str5

      return result

print ("Первый вызов: ")
result1 = combine_string ("Я", "люблю", "Python")
print("Результат:", result1)


return_string()
square_number()
return_string()
