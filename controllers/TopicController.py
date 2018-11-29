from models.answerStatus import AnswerStatus
from models.question import Question
from models.account import Account
from sqlalchemy import update
from models.model import db
import datetime

def createTopic(question, accountId, answerStatusId, isPoll):
    question = Question()
    question.Question = question
    question.AccountId = accountId
    question.TimeStamp = datetime.date.today()
    question.AnswerStatusId = answerStatusId
    question.IsPoll = isPoll
    question.Score = 0

    db.session.add(question)
    db.session.commit()

    return question

def findAllTopic():
    return Question.query.all()

def findById(id):
    return Question.query.get(id)

def updateTopicScore(id, value):
    question = findById(int(id))
    if question == None:
        return 'erreur!'

    question.Score = question.Score + int(value)

    db.session.add(question)
    db.session.commit()

    return question.Score

def deleteTopicController(questionId):
    print('delete topic not implemented')

    Question.query.filter_by(id = questionId).delete()
    db.session.commit()
