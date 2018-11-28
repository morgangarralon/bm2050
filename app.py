
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

from controllers import TopicController

static_url_path = '/static'
app = Flask(__name__, static_url_path=static_url_path)
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello, world!'

# @app.route('/test')
# def hello_test():
#     return 'Hello, TEST!'

# @app.route('/template')
# def templates():
#     return render_template('sample.html', title='template test')

@app.route('/addTopic', methods = ['GET', 'POST'])
def addTopic():
    if request.method == 'GET':
        return render_template('AddTopic.html', title='template test')
    elif request.method == 'POST':
        TopicController.createTopic(request.form.get('question'), 1, 1, True)
        return render_template('AddTopic.html', title='template test')

# @app.route('/models')
# def models():
#     a = Account('toto@tt.fr')
#     a.Password = 'helloworld'
#     return '<p> {} </p>'.format(a.EmailAddress)

@app.route('/index')
def indexzouille():

    topics = TopicController.findAllTopic()
    #= ['bla', 'blabla', 'blablabla', '...............................................................']
    return render_template('index.html', static_url_path = static_url_path, topic_list='lol', topics = topics)

@app.route('/topic')
def indexzouille():

    topics = TopicController.findAllTopic()
    #= ['bla', 'blabla', 'blablabla', '...............................................................']
    return render_template('topic.html', static_url_path = static_url_path, topic_list='lol', topics = topics)



if __name__ == '__main__':
    app.run('localhost', '5000')
