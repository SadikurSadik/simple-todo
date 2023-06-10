from app import db


class Todo(db.Model):
    __tablename__ = "poridhian"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    todo = db.Column(db.Text)
    is_completed = db.Column(db.Boolean)

    def __init__(self, data):
        self.data = data