
from flask import (
    Flask, flash, render_template, redirect, request, url_for, session, jsonify
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
from controllers import AccountController

static_url_path = '/static'
app = Flask(__name__, static_url_path=static_url_path)
app.debug = True
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=model.database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=model.track_modification
)

model.init_app(app)

#loggedInAccount = None

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def hello_world():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    topics = TopicController.findAllTopic()
    return render_template('index.html', static_url_path = static_url_path, topics = topics)

@app.route('/add_topic', methods = ['GET', 'POST'])
def add_topic():
    template = None
    if request.method == 'GET':
        template = render_template('add_topic.html')
    elif request.method == 'POST':
        topic = TopicController.createTopic(request.form.get('question'), 1, 1, True)
        if topic == None:
            template = render_template('404.html', title = "Erreur dans l'affichage du topic " + topic_id)
        else:
            template = render_template('topic.html', topic = topic)

    return template

@app.route('/login', methods=['GET', 'POST'])
def do_login():
    try:
        account = Account.query.filter_by(EmailAddress == request.form['username'])
        if request.form['password'] == account.password:
            session['logged_in'] = True
        else:
            flash('L\'email ou le mot de passe est/sont erroné(s) !')
    except:
            print("Exception login")
    return index()

@app.route('/register', methods = ['GET', 'POST'])
def register():
    template = None
    if request.method == 'GET':
        template = render_template('register.html')
    elif request.method == 'POST':
        # TODO passwordCheck

        oggedInAccount = AccountController.createAccount(
            request.form.get('firstName'),
            request.form.get('lastName'),
            request.form.get('emailAddress1'),
            request.form.get('username'),
            request.form.get('password1')
        )
        template = render_template('index.html', static_url_path = static_url_path, topics = TopicController.findAllTopic())

    return template

@app.route('/_update_topic_score/')
def update_topic_score():
    value = request.args.get('value', 0, type=int)
    topic_id = request.args.get('topic_id', 0, type=int)
    score = TopicController.updateTopicScore(topic_id, value)

    return jsonify(result=score)

@app.route('/display_topic/<topic_id>')
def display_topic(topic_id = None):
    topic = TopicController.findById(topic_id)
    if topic is None:
        template = render_template('404.html', title = "Erreur dans l'affichage du topic " + topic_id)

    return render_template('topic.html', topic = topic)


if __name__ == '__main__':
    app.run('localhost', '5000')
