from models.answerStatus import AnswerStatus
from models.account import Account
from models.answer import Answer
from models.pollOption import PollOption
from sqlalchemy import update
from models.model import db
import datetime

def createAnswer(questionId, accountId, answer, pollStatus):
    answ = Answer()

    answ.QuestionId = questionId
    answ.AccountId = accountId
    answ.Answer = answer
    answ.TimeStamp = datetime.date.today()
    answ.Score = 0
    poll = PollOption.query.filter_by(PollOptionName=pollStatus).first()
    answ.PollOptionId = poll.Id
    db.session.add(answ)
    db.session.commit()

    return answ

def getAnswersByQuestionId(id):
    return Answer.query.filter_by(QuestionId=id).all()
