from .model import db

class DomainExpertise(db.Model):
    __tablename__ = 'DomainExpertise'
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))

    def __repr__(self):
        return '<domainExpertise %r>'% self.Name

