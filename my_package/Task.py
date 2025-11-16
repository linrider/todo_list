class Task:
    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed
        
    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.id}, {self.title}"
    
    