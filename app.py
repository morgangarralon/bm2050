
from flask import (
    Flask, render_template, redirect, request, url_for, session, jsonify
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
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=model.database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=model.track_modification
)

model.init_app(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def hello_world():
    topics = TopicController.findAllTopic()
    return render_template('index.html', static_url_path = static_url_path, topics = topics)

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

@app.route('/_update_topic_score/')
def update_topic_score():
    value = request.args.get('value', 0, type=int)
    topic_id = request.args.get('topic_id', 0, type=int)
    score = TopicController.updateTopicScore(topic_id, value)

    return jsonify(result=score)

@app.route('/display_topic/<topic_id>')
def display_topic(topic_id = None):
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
