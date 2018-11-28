
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

@app.route('/displayTopic/<topic_id>')
def displayTopic(topic_id = None):
    template = None;

    try:
        topic = TopicController.findById(topic_id)

        if topic == None:
            template = render_template('404.html', title = "Erreur dans l'affichage du topic " + topic_id)
    except ModuleNotFoundError as e:
        template = render_template('404.html', title = "Erreur dans l'affichage du topic " + topic_id)

    template = render_template('topic.html', topic = topic)

    return template


if __name__ == '__main__':
    app.run('localhost', '5000')
