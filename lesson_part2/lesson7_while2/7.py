# В компании решили запустить новую акцию: каждый день первые два покупателя получают скидку 20%.
# Напиши программу для распределения скидок.
#
# Программа должна:
# 1. Запросить номер карты.
# 2. Первым двум покупателям напечатать: «Поздравляем! Вы получили скидку 20%.»
# 3. Всем остальным напечатать: «Скидки закончились.» и завершить работу.
#
# Пример работы программы:

# Введите номер карты:>? 12314
# Поздравляем! Вы получили скидку 20%.
# Введите номер карты:>? 14124
# Поздравляем! Вы получили скидку 20%.
# Скидки закончились.

card = input("Введите номер карты: ")
count = 0
while count < 2:
    print("Поздравляем! Вы получили скидку 20%.")
    count += 1
    card = input("Введите номер карты:")
print("Скидки закончились.")