
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
from controllers import AnswerController

static_url_path = '/static'
app = Flask(__name__, static_url_path=static_url_path)
app.debug = True
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=model.database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=model.track_modification
)
app.secret_key = "azedqolikncvr65g5215pverbepouh"

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
    return render_template('index.html', static_url_path=static_url_path,
            topics=topics, session=session)

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

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def do_login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        account = Account.query.filter_by(EmailAddress=request.form['username']).first()
        if account is not None and request.form['password'] == account.Password:
            session['account_id'] = account.Id
            session['account_username'] = account.Username
            session['logged_in'] = True
        else:
            flash("e-mail ou mot de passe invalide !")
            return redirect(url_for('do_login'))
    return redirect(url_for('index'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
    template = None
    if request.method == 'GET':
        template = render_template('register.html')
    elif request.method == 'POST':
        # TODO passwordCheck

        if (request.form.get('emailAddress1') == request.form.get('emailAddress2')):
            print("emails correspond")
        else:
            print("emails don't correspond")

        if(request.form.get('password1') == request.form.get('password2')):
            print("passwords correspond")
        else:
            print("emails don't correspond")

        AccountController.createAccount(
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

@app.route('/add_comment/<question_id>')
def add_comment(question_id = None):
    #accountId = request.args.get('account_id', 0, type=int)
    accountId = 1
    questionId = request.args.get('question_id', 0, type=int)
    answer = request.args.get('answer', type=string)
    AnswerController.createAnswer(question_id, account_id, answer)
    return display_topic(question_id)


@app.route('/display_topic/<topic_id>')
def display_topic(topic_id = None):
    template = None
    try:
        topic = TopicController.findById(topic_id)
        if topic == None:
            template = render_template('404.html', title = "Erreur dans l'affichage du topic " + topic_id)
    except ModuleNotFoundError as e:
        template = render_template('404.html', title = "Erreur dans l'affichage du topic " + topic_id)

    return render_template('topic.html', topic = topic)

@app.route('/about')
def about():
    topics = TopicController.findAllTopic()
    return render_template('about.html', static_url_path = static_url_path, topics = topics)

if __name__ == '__main__':
    app.run('localhost', port =5000)
