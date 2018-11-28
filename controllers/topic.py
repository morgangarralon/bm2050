import datetime

from models.answerStatus import AnswerStatus
from models.account import Account
from models.model import db
from models.question import Question


class Topic(object):
    def __init__(self, question, accountId, answerStatusId, isPoll):
        qst = Question()

        qst.Question = question
        qst.AccountId = accountId
        qst.TimeStamp = datetime.date.today()
        qst.AnswerStatusId = answerStatusId
        qst.IsPoll = isPoll
        qst.Score = 0
        self.qst = qst

    def save(self):
        db.session.add(self.qst)
        db.session.commit()

    def delete(self):
        print('delete topic not implemented')


class Topics(object):
    @staticmethod
    def get_all():
        topics = ['blah', 'blabla']
        return topics
