from .model import db

class Answer(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    QuestionId = db.Column(db.Integer, db.ForeignKey('question.id'))
    AccountId = db.Column(db.Integer, db.ForeignKey('account.id'))
    Answer = db.Column(db.String(1000))
    AnswerId = db.Column(db.Integer, db.ForeignKey('answer.id'))
    TimeStamp = db.Column(db.DateTime)
    PollOptionId = db.Column(db.Integer, db.ForeignKey('pollOption.id'))
    Score = db.Column(db.Integer)

    def __repr__(self):
        return '<answer %r>'% self.answer

