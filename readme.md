pip install flask-sqlalchemy
pip install flask-migrate

flask db init
flask db migrate -m "user table"
flask db upgrade  create the table
flask db downgrade  undo the change

flask db history
flask db current


delete data:

users = User.query.all()
>>> for u in users:
...     db.session.delete(u)
db.session.commit()

posts = Post.query.all()
>>> for p in posts:
...     db.session.delete(p)
>>> db.session.commit()
db.session.commit()

password hash
from werkzeug.security import generate_password_hash, check_password_hash
hash = gererate_password_hash('testing')
check_password_hash(hash, 'testing')
return true

u = User(username='Echo', email='echo@demo.com')
>>> u.set_password('testing')
>>> u.check_password('password')
False
>>> u.check_password('testing')

pip install flask-login

UserMixin
