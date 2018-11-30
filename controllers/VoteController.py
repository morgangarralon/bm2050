from models.answerStatus import AnswerStatus
from models.question import Question
from models.account import Account
from models.vote import Vote
from sqlalchemy import update
from models.model import db
import datetime

def createQuestionVote(accountId, questionId, value):
    vote = Vote()

    vote.AccountId = accountId
    vote.QuestionId = questionId
    vote.TimeStamp = datetime.datetime.now()
    if value is 1:
        vote.IsUpvote = True
    else:
        vote.IsUpvote = False

    db.session.add(vote)
    db.session.commit()

    return vote

def findQuestionVote(accountId, questionId):
    return Vote.query.filter_by(AccountId=accountId, QuestionId=questionId).first()

def findAnswerVote(accountId, answerId):
    return Vote.query.filter_by(AccountId=accountId, AnswerId=answerId).first()

def findAllVote():
    return Vote.query.all()

def findById(id):
    return Vote.query.get(id)