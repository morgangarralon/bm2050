from .model import db

class PollOption(db.Model):
    __tablename__ = 'PollOption'
    Id = db.Column(db.Integer, primary_key=True)
    PollOptionName = db.Column(db.String(255))
    QuestionId = db.Column(db.Integer, db.ForeignKey('Question.Id'))
