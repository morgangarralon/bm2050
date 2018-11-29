from models.answerStatus import AnswerStatus
from models.question import Question
from models.account import Account
from sqlalchemy import update
from models.model import db
import datetime

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

    return qst

def findAllTopic():
    return Question.query.all()

def findById(id):
    return Question.query.get(id)

def updateTopicScore(id, value):
    question = findById(int(id))
    if question is None:
        raise RuntimeError('question not found')
    question.Score = question.Score + int(value)
    db.session.commit()
    return question.Score

def deleteTopicController(questionId):
    print('delete topic not implemented')
    Question.query.filter_by(id = questionId).delete()
    db.session.commit()
