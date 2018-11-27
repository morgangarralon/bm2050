
from flask import (
    Flask, render_template, redirect, request, url_for, session
)

from models import model
from models.account import Account
from models.accountDomainExpertise import AccountDomainExpertise
from models.answer import Answer
from models.answerDomainExpertise import AnswerDomainExpertise
from models.answerStatus import AnswerStatus
from models.domainExpertise import DomainExpertise
from models.pollOption import PollOption
from models.question import Question
from models.role import Role
from models.vote import Vote



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/test')
def hello_test():
    return 'Hello, TEST!'

@app.route('/template')
def templates():
    return render_template('sample.html', title='template test')

@app.route('/models')
def models():
    a = Account('toto@tt.fr')
    a.Password = 'helloworld'
    return '<p> {} </p>'.format(a.EmailAddress)


if __name__ == '__main__':
    app.run()
