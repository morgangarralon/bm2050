from models.account import Account
from functools import wraps
from flask import request, Response
from models.model import db

import datetime

def createAccount(firstName, lastName, emailAddress, username, password):

    account = Account()

    account.IsAdmin = False
    account.FirstName = firstName
    account.LastName = lastName
    account.EmailAddress = emailAddress
    account.RoleId = 1
    account.CreationDate = datetime.datetime.now()
    account.LastLogin = datetime.datetime.now()
    account.Username = username
    account.Password = password

    db.session.add(account)
    db.session.commit()

def deleteAccount():
    print('Account deletion not yet implemented')

# The @login_manager.user_loader piece tells Flask-login how to load users given an id
#    @login_manager.user_loader
#    def user_loader(AccountId):
#        return Account.query.get(AccountId)
#
#    def isConnected():
#        if session.get('logged_in') == True:
#            return 'Logout'
#        return 'Login'
