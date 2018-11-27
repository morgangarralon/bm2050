from .model import db

class AnswerDomainExpertise(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    DomainExpertiseId = db.Column(db.Integer, db.ForeignKey('domainExpertise.id'))

    def __repr__(self):
        return '<answerDomainExpertise %r>'% self.Id

