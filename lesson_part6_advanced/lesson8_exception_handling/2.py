# Создайте функцию, которая запрашивает у пользователя ввод числа.
# Если введено не число, обработайте исключение и попросите ввести число повторно.
while True:
    a = input('Число: ')
    try:
        a = int(a)
        break
    except ValueError:
        print("Напишите число, а не строку!")
print('Программа завершена!')