#!/usr/bin/env python3

from flask import Flask
from models import model
from models.account import Account
from models.question import Question
from models.answerStatus import AnswerStatus
from models.domainExpertise import DomainExpertise
from models.accountDomainExpertise import AccountDomainExpertise
from models.pollOption import PollOption

import datetime

app = Flask(__name__)
app.debug = True
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=model.database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=model.track_modification
)

model.init_app(app)

# help(model)

acc = Account()
acc.IsAdmin = False
acc.FirstName = 'Erik'
acc.LastName = 'Stevens'
acc.EmailAddress = 'erik@stevens.fr' # pas un vrai ... malheureusement
acc.RoleId = 1
acc.CreationDate = datetime.datetime.now()
acc.LastLogin = datetime.datetime.now()
acc.Username = 'Erik'
acc.Password = 'Stevens'
model.db.session.add(acc)

acc = Account()
acc.IsAdmin = False
acc.FirstName = 'a'
acc.LastName = 'a'
acc.EmailAddress = 'a@a.a' # pas un vrai ... malheureusement
acc.RoleId = 1
acc.CreationDate = datetime.datetime.now()
acc.LastLogin = datetime.datetime.now()
acc.Username = 'a'
acc.Password = 'a'
model.db.session.add(acc)

acc = Account()
acc.IsAdmin = False
acc.FirstName = 'a'
acc.LastName = 'a'
acc.EmailAddress = 'b@a.a' # pas un vrai ... malheureusement
acc.RoleId = 1
acc.CreationDate = datetime.datetime.now()
acc.LastLogin = datetime.datetime.now()
acc.Username = 'b'
acc.Password = 'b'
model.db.session.add(acc)

ans = AnswerStatus()
ans.Name = 'Done'

model.db.session.add(ans)
model.db.session.commit()

questions = [
    'LE BEC DE BONNE ESPÉRANCE À AMBÈS',
    'DES GALERIES TECHNIQUES MAGIQUES À BORDEAUX',
    '« VAGUE REBELLE ET PISCINE GÉANTE SUR LA GARONNE » À BORDEAUX',
]
for i in range(len(questions)):
    question = Question()
    question.TimeStamp = datetime.date.today()
    question.AnswerStatusId = 1
    question.IsPoll = True
    question.Score = 0
    question.AccountId = i + 1
    question.Question = questions[i]
    model.db.session.add(question)
    model.db.session.commit()


for domain in ['voierie', 'environnement', 'politique',
        'sociologue', 'philosophe', 'économie']:
    d = DomainExpertise()
    d.Name = domain
    model.db.session.add(d)
model.db.session.commit()

accountDomainExpertise = AccountDomainExpertise()
accountDomainExpertise.DomainExpertiseId = 1
accountDomainExpertise.AccountId = 2
model.db.session.add(accountDomainExpertise)


poll1 = PollOption()
poll1.PollOptionName = "Pour"

poll2 = PollOption()
poll2.PollOptionName = "Contre"

model.db.session.add(poll1)
model.db.session.add(poll2)
model.db.session.commit()
