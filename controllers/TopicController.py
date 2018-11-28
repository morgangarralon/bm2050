import datetime

from models.answerStatus import AnswerStatus
from models.account import Account
from models.model import db
from models.question import Question

def createTopic(question, accountId, answerStatusId, isPoll):

    qst = Question()

    qst.Question = question
    qst.AccountId = accountId
    qst.TimeStamp = datetime.date.today()
    qst.AnswerStatusId = answerStatusId
    qst.IsPoll = isPoll
    qst.Score = 0

    db.session.add(qst)
    db.session.commit()

def findAllTopic():
    return Question.query.all()

def DeleteTopicController(questionId):
    print('delete topic not implemented')
    
    Question.query.filter_by(id = questionId).delete()
    db.session.commit()
