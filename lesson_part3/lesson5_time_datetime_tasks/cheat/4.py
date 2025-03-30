"""напишите программу секундомер. она должна запускать отсчёт времени при нажатии клавиши 1, заканчивать его при
нажатии клавиши 0. на остальные клавиши реакции быть не должно

Пример:

1 - старт. 0 - стоп:>? 1
0 - стоп:>? в
0 - стоп:>? 0
Общее время: 5 c
"""

from time import time

flag = input('1 - старт. 0 - стоп:')
while flag != '0':
    if flag == '1':
        start = time()
    flag = input('0 - стоп:')
end = time()
total = round(end - start, 3)
print('Общее время:', total, 'c')
