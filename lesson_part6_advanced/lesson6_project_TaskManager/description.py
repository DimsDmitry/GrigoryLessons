"""▎Проект: "Менеджер задач"

Описание проекта: Создайте простое приложение для управления задачами, где пользователь может добавлять,
удалять и просматривать задачи. Задачи будут храниться в списке, а метки для задач — в множестве. Для хранения
истории изменений можно использовать кортежи.

Требования:

1. Создайте класс TaskManager, который будет представлять менеджер задач:

   • Атрибуты:

     • tasks (список) — список текущих задач.

     • tags (множество) — множество уникальных меток для задач.

     • history (список кортежей) — список для хранения истории изменений (например, добавление или удаление задачи).

   • Методы:

     • add_task(task, tag) — добавляет задачу с меткой.

     • remove_task(task) — удаляет задачу.

     • view_tasks() — отображает текущие задачи и их метки.

     • view_history() — показывает историю изменений.

2. Реализуйте простой интерфейс командной строки, который позволит пользователю взаимодействовать с менеджером задач:

   • Пользователь может добавлять задачи, удалять их и просматривать текущие задачи и историю."""