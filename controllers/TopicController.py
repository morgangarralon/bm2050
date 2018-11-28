import datetime

from models.answerStatus import AnswerStatus
from models.account import Account
from models.model import db
from models.question import Question
from sqlalchemy import update

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

def findById(id):
    return Question.query.get(id)

def updateTopicScore(id, vote):
    question = findById(int(id))
    question.Score = question.Score + int(vote)
    db.session.commit()

def DeleteTopicController(questionId):
    print('delete topic not implemented')

    Question.query.filter_by(id = questionId).delete()
    db.session.commit()
