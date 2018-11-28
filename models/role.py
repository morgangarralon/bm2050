from .model import db

class Role(db.Model):
    __tablename__ = 'Role'
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))

    def __repr__(self):
        return '<role %r>'% self.Name

