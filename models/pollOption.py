from .model import db

class PollOption(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    QuestionName = db.Column(db.String(255))
    QuestionId = db.Column(db.Integer, db.ForeignKey('question.id'))

    def __repr__(self):
        return '<pollOption %r>'% OptionName

