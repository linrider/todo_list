# from my_package.TodoList import TodoList
# from my_package.Task import Task
 
# def main():
#     todo_list = TodoList()
    
# if __name__ == "__main__":
#     main()
class Task:
    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed
        
    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.id}: {self.title}"


class TodoList:
    def __init__(self):
        self.tasks: list[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str) -> Task:
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        if not self.tasks:
            print("Список задач порожній.")
            return
        for task in self.tasks:
            print(task)

    def complete_task(self, task_id: int):
        task = self._find_task(task_id)
        if task is None:
            print(f"Задачу з id={task_id} не знайдено.")
            return
        task.completed = True
        print(f"Задача {task_id} відмічена як виконана.")

    def delete_task(self, task_id: int):
        task = self._find_task(task_id)
        if task is None:
            print(f"Задачу з id={task_id} не знайдено.")
            return
        self.tasks.remove(task)
        print(f"Задачу {task_id} видалено.")

    def _find_task(self, task_id: int) -> Task | None:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None


def main():
    todo = TodoList()
    while True:
        print("\nКоманди:")
        print("1 - показати задачі")
        print("2 - додати задачу")
        print("3 - відмітити як виконану")
        print("4 - видалити задачу")
        print("0 - вихід")

        cmd = input("Введи команду: ").strip()

        if cmd == "1":
            todo.list_tasks()
        elif cmd == "2":
            title = input("Назва задачі: ").strip()
            if not title:
                print("Назва не може бути порожньою.")
                continue
            task = todo.add_task(title)
            print(f"Додано: {task}")
        elif cmd == "3":
            try:
                task_id = int(input("ID задачі: "))
            except ValueError:
                print("ID має бути числом.")
                continue
            todo.complete_task(task_id)
        elif cmd == "4":
            try:
                task_id = int(input("ID задачі: "))
            except ValueError:
                print("ID має бути числом.")
                continue
            todo.delete_task(task_id)
        elif cmd == "0":
            print("Бувай 👋")
            break
        else:
            print("Невідома команда.")


if __name__ == "__main__":
    main()
