import datetime

from models.account import Account
from models.model import db
from models.question import Question
from models.pollOption import PollOption

def createAnswer(answer, accountId, questionId, PollOptionId):

    newAnswer = Answer()

    newAnswer.Answer = answer
    newAnswer.AccountId = accountId
    newAnswer.TimeStamp = datetime.date.today()
    newAnswer.QuestionId = questionId
    newAnswer.PollOptionId = PollOptionId
    newAnswer.Score = 0

    db.session.add(newAnswer)
    db.session.commit()


def updateAnswer(AnswerId):
    print ('Answer update not yet implemented')

def deleteAnswer(AnswerId):
    print('Answer deletion not yet implemented')
