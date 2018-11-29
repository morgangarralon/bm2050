from models.answerStatus import AnswerStatus
from models.question import Question
from models.account import Account
from sqlalchemy import update
from models.model import db
import datetime

def createAnswer(questionId, accountId, answer):
    answ = Answer()

    answ.QuestionId = questionId
    answ.AccountId = accountId
    answ.Answer = answer
    answ.TimeStamp = datetime.date.today()
    answ.Score = 0

    db.session.add(answ)
    db.session.commit()

    return answ
