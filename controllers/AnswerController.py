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
    account = Account.query.filter_by(Id=accountId).first()
    account.setDomainExpertise()
    if len(account.DomainExpertise) > 0:
        answ.IsExpert = True
    else:
        answ.IsExpert = False
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

def getAnswerByIdAndPollOrderedByExpertise(id, pollValue):
    poll = PollOption.query.filter_by(PollOptionName=pollValue).first()
    print("!!! " + str(pollValue) + " !!!")
    print("!!! " + str(poll.Id) + " !!!")
    return Answer.query.filter_by(QuestionId=id, PollOptionId=poll.Id).order_by(Answer.IsExpert.asc())

def updateAnswerScore(id, value):
    answer = findById(int(id))
    if answer is None:
        raise RuntimeError('question not found')
    answer.Score = answer.Score + int(value)
    db.session.commit()
    return answer.Score