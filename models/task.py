class Task:
    def __init__(self, title, deadline, priority="medium"):
        self.title = title
        self.deadline = deadline
        self.priority = priority
        self.status = "pending"

    def to_dict(self):
        return {
            "title": self.title,
            "deadline": self.deadline,
            "priority": self.priority,
            "status": self.status
        }
