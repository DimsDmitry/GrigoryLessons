# Напиши программу, которая запрашивает фамилию автора.
#
# 1. Если фамилия есть в словаре (ключ), то печатается слово «Биография:» и затем биография автора (значение ключа).
#
# 2. Если фамилии нет, то программа выводит: «Автор не найден. Добавить?». 2.1. Если пользователь отвечает «Да»,
# то запрашивается ввод биографии. Затем автор и его биография добавляется в каталог. 2.2. Если пользователь не хочет
# добавлять автора, то программа печатает: «Ответ получен» и завершает работу.

authors = {
    'Пушкин': 'Русский поэт, драматург и прозаик. Один из самых авторитетных литературных деятелей XIX века',
    'Толстой': 'Один из наиболее известных русских писателей и мыслителей, один из величайших писателей-романистов мира',
    'Бунин': 'Русский писатель, поэт и переводчик, лауреат Нобелевской премии по литературе 1933 года'
    }


surname = input('Введите фамилию автора:')
if surname in authors:
    print('Биография:', authors[surname])
else:
    answer = input('Автор не найден! Хотите его добавить?')
    if answer == 'да':
        biography = input('Введите его биографию:')
        authors[surname] = biography
    else:
        print('Ответ получен.')

print(authors)
