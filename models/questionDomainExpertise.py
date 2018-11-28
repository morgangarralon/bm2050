from .model import db

class QuestionDomainExpertise(db.Model):
    __tablename__ = 'QuestionDomainExpertise'
    Id = db.Column(db.Integer, primary_key=True)
    DomainExpertiseId = db.Column(db.Integer, db.ForeignKey('domainExpertise.id'))

    def __repr__(self):
        return '<questionDomainExpertise %r>'% self.Id

