from .model import db

class AccountDomainExpertise(db.Model):
    __tablename__ = 'AccountDomainStatus'
    AccountId = db.Column(db.Integer, primary_key=True)
    DomainExpertiseId = db.Column(db.Integer, db.ForeignKey('domainExpertise.id'))

    def __repr__(self):
        return '<accountDomainExpertise %r>'% self.AccountId
