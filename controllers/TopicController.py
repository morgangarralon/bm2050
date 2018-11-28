from models.model import db
from models.question import Question
from models.answerStatus import AnswerStatus

import datetime

def createTopic(topic):
    
    qst = Question()

    qst.Question = topic.get('question')
    qst.TimeStamp = datetime.date.today()
    qst.AccountId = 1
    qst.IsPoll = False
    qst.AnswerStatusId = 1
    qst.Score = 100

    db.session.add(qst)
    db.session.commit()

    print("Le sujet a été crée")

def DeleteTopicController(topic):
    print("Le sujet a été supprimé")
