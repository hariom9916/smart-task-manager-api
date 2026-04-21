from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    deadline = db.Column(db.String(50))
    priority = db.Column(db.String(20))
    status = db.Column(db.String(20))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "deadline": self.deadline,
            "priority": self.priority,
            "status": self.status
        }
