

from models.model import db
from models.account import Account

for email in ['toto@epsi.fr', 'titi@epsi.fr']:
    a = Account(email)
    a.IsAdmin = False
    a.FirstName = email
    db.session.add(a)
    db.session.commit()

print(Account.query.all())

