from .model import db

class Question(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.String(1000))
    TimeStamp = db.Column(db.DateTime)
    AnswerStatusId = db.Column(db.Integer, db.ForeignKey('answerStatus.id'))
    IsPoll = db.Column(db.Boolean)

    def __repr__(self):
        return '<question %r>'% self.Question

