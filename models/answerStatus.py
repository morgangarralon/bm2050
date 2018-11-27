from .model import db

class AnswerStatus(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))

    def __repr__(self):
        return '<answerStatus %r>'% self.Name

