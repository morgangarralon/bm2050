from .model import db

class Vote(db.Model):
    __tablename__ = 'Vote'
    Id = db.Column(db.Integer, primary_key=True)
    IsUpvote = db.Column(db.Boolean)
    TimeStamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<vote %r>'% self.Id
