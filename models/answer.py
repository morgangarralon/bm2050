from .model import db

class Answer(db.Model):
    __tablename__ = 'Answer'
    Id = db.Column(db.Integer, primary_key=True)
    QuestionId = db.Column(db.Integer, db.ForeignKey('Question.Id'))
    AccountId = db.Column(db.Integer, db.ForeignKey('Account.Id'))
    Answer = db.Column(db.String(1000))
    AnswerId = db.Column(db.Integer, db.ForeignKey('Answer.Id'))
    TimeStamp = db.Column(db.DateTime)
    PollOptionId = db.Column(db.Integer, db.ForeignKey('PollOption.Id'))
    Score = db.Column(db.Integer)
    IsExpert = db.Column(db.Boolean)
