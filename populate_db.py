#!/usr/bin/env python3

from models.model import db
from models.account import Account
from models.answerStatus import AnswerStatus

import datetime


acc = Account()
acc.IsAdmin = False
acc.FirstName = 'Erik'
acc.LastName = 'Stevens'
acc.EmailAddress = 1
acc.RoleId = 1
acc.CreationDate = datetime.datetime.now()
acc.LastLogin = datetime.datetime.now()
acc.Username = 'Erik'
acc.Password = 'Stevens'

db.session.add(acc)
db.session.commit()

ans = AnswerStatus()
ans.Name = 'Done'

db.session.add(ans)
db.session.commit()