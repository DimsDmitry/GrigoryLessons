# Работа с индексами списка:
# Создайте список из 5 элементов и напишите программу,
# которая запрашивает индекс элемента. Обработайте исключение, если индекс выходит за пределы списка.
strr = ["Hello", 52, 123, 1.5, "aloxa"]
while True:
    index = int(input("Введите индекс эллемента: "))
    try:
        print(strr[index])
    except IndexError:
        print("Такого индекса в списке нету.")