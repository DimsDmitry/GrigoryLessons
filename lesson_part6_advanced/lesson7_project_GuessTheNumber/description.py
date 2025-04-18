"""Проект: "Игра в угадай число"

Описание проекта: Создайте простую игру, в которой компьютер загадывает число, а пользователь пытается его угадать.
Игра будет использовать классы, циклы и условные операторы.

Требования:

1. Создайте класс GuessingGame, который будет представлять игру:

   • Атрибуты:

     • number_to_guess (целое число) — загаданное число.

     • attempts (целое число) — количество попыток, которые пользователь уже сделал.

   • Методы:

     • start_game() — запускает игру, генерируя случайное число и позволяя пользователю делать попытки.

     • make_guess(guess) — принимает предположение пользователя и проверяет его.

     • is_correct(guess) — возвращает True, если угадано правильно, иначе False.

2. Реализуйте простой интерфейс командной строки, который позволит пользователю взаимодействовать с игрой:

   • Пользователь может вводить свои догадки.

   • Игра должна сообщать пользователю, больше или меньше загаданное число по сравнению с его предположением.

   • Игра продолжается до тех пор, пока пользователь не угадает число."""