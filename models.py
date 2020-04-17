import datetime
from exts import db


class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(20), nullable=False)
	password = db.Column(db.String(20), nullable=False)
	disk_use = db.Column(db.Float, default=0, nullable=False)
	is_staff = db.Column(db.Boolean, default=False, nullable=False)

	messages = db.relationship('Message', backref='author')

	def __repr__(self):
		return self.username


class Message(db.Model):
	__tablename__ = 'message'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	kernel_use = db.Column(db.Integer, default=1, nullable=False)
	memory_use = db.Column(db.Float, default=0, nullable=False)
	time_begin = db.Column(db.DateTime, default=datetime.datetime.now())
	time_end = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=True)
	comment = db.Column(db.String(200), nullable=True)

	uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	# author = db.relationship('User', backref='messages')
