
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

from controllers.topic import Topics, Topic


static_url_path = '/static'
app = Flask(__name__, static_url_path=static_url_path)
app.debug = True
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=model.database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=model.track_modification
)

model.db.init_app(app)


@app.route('/')
def hello_world():
    return redirect(url_for('index'))


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
def index():
    topics = Topics.get_all()
    return render_template('index.html', static_url_path=static_url_path, topics=topics)

# Route de login. Redirige vers index
@app.route('/login', methods=['POST'])
def do_login():
    try:
        account = Account.query.filter_by(EmailAddress == request.form['username'])
        if request.form['password'] == account.password:
            session['logged_in'] = True
        else:
            flash('L\'email ou le mot de passe est/sont erroné(s) !')
    return index()


@app.route('/displayTopic/<topic_id>')
def displayTopic(topic_id = None):
    topic = Topic.get_by_id(1)
    if topic is None:
        return render_template('404.html', title = "Erreur dans l'affichage du topic " + topic_id)
    return render_template('topic.html', topic = topic)


if __name__ == '__main__':
    app.run('localhost', '5000')
