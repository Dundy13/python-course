def add_task():
    task_name = input("Въведете име на задачата: ")
    tasks.append(task_name)
    print(f'Задачата "{task_name}" беше добавена успешно.\n')


def view_tasks():
    if not tasks:
        print("Няма текущи задачи.")
    else:
        print("Текущи задачи:")
        for i, task in enumerate(tasks, start=1):
            print(f'{i}. {task}')
        print()

        def delete_task():
    view_tasks()
    if not tasks:
        print("Няма задачи за изтриване.")
    else:
        try:
            task_index = int(input("Изберете номер на задачата за изтриване: "))
            if 1 <= task_index <= len(tasks):
                deleted_task = tasks.pop(task_index - 1)
                print(f'Задачата "{deleted_task}" беше изтрита успешно.\n')
            else:
                print("Грешен номер на задача. Опитайте отново.")
        except ValueError:
            print("Невалиден вход. Моля, въведете номер на задачата (цяло число).\n")


            while True:
    print("Меню:")
    print("1. Добавяне на задача")
    print("2. Преглеждане на задачи")
    print("3. Изтриване на задача")
    print("4. Изход")

    choice = input("Изберете опция (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Благодарим за използването на приложението. Довиждане!")
        break
    else:
        print("Грешен избор. Моля, въведете число от 1 до 4.")