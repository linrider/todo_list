from my_package.Task import Task


class TodoList:
    def __init__(self):
        self.tasks: list[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str) -> Task:
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        return task
        