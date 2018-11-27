from .model import db

class Vote(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    AccountId = db.Column(db.Integer, db.ForeignKey('account.id'))
    AnswerId = db.Column(db.Integer, db.ForeignKey('answer.id'))
    QuestionId = db.Column(db.Integer, db.ForeignKey('question.id'))
    TimeStamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<vote %r>'% self.Id

