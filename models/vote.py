from .model import db

class Vote(db.Model):
    __tablename__ = 'Vote'
    Id = db.Column(db.Integer, primary_key=True)
    AccountId = db.Column(db.Integer, db.ForeignKey('Account.Id'))
    AnswerId = db.Column(db.Integer, db.ForeignKey('Answer.Id'))
    QuestionId = db.Column(db.Integer, db.ForeignKey('Question.Id'))
    IsUpvote = db.Column(db.Boolean)
    TimeStamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<vote %r>'% self.Id

