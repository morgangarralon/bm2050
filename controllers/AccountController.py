from models.account import Account
from functools import wraps
from flask import request, Response

def createAccount():
    print('Account creation not yet implemented')

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
