from .model import db
from models.answer import Answer
from controllers import AnswerController

class Question(db.Model):
    __tablename__ = 'Question'
    Id = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.String(1000))
    AccountId = db.Column(db.Integer, db.ForeignKey('Account.Id'))
    TimeStamp = db.Column(db.DateTime)
    AnswerStatusId = db.Column(db.Integer, db.ForeignKey('AnswerStatus.Id'))
    IsPoll = db.Column(db.Boolean)
    Score = db.Column(db.Integer)
    Answers = []

    def __init__(self):
        print("New question created!")

    def __repr__(self):
        return '<question %r>'% self.Question

    def setAnswers(self):
        self.Answers = AnswerController.getAnswersByQuestionId(self.Id)
