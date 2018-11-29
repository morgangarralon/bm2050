from flask import Flask
from models import model
from models.account import Account
from models.question import Question
from models.answerStatus import AnswerStatus
from models.domainExpertise import DomainExpertise

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

ans = AnswerStatus()
ans.Name = 'Done'

model.db.session.add(ans)
model.db.session.commit()

question = Question()
question.Question = 'test tse'
question.AccountId = 1
question.TimeStamp = datetime.date.today()
question.AnswerStatusId = 1
question.IsPoll = True
question.Score = 0

question2 = Question()
question2.Question = 'test tse'
question2.AccountId = 2
question2.TimeStamp = datetime.date.today()
question2.AnswerStatusId = 1
question2.IsPoll = True
question2.Score = -99

model.db.session.add(question)
model.db.session.add(question2)
model.db.session.commit()


for domain in ['voierie', 'environnement', 'politique',
        'sociologue', 'philosophe', 'economie']:
    d = DomainExpertise()
    d.Name = domain
    model.db.session.add(d)
model.db.session.commit()


