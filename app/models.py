#models for app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import loginmanager,db

class students():
"""create students table in database"""
    __tablename__='Students'
    id=db.Column(db.Integer,primary_key=True)
	first_name=db.Column(db.String(60),index=True)
	last_name=db.Column(db.String(60),index=True)
	email=db.Column(db.String(60),Index=True,unique=True)
	phone=db.Column(db.Integer,index=True,unique=True)
	password_hash=db.Column(db.String(128))
	is_admin=db.Column(db.Boolean,default=True)
	
	@property
	def password(self):
	   raise AttributeError('Password is not visible')
	   
	@password.setter
    def set_password(self,password):
	"""sets password into a hashed password"""
        self.password_hash = generate_password_hash(password)	
		
	@password.check
	def check_password(self,password):
	    return check_password_hash(self.password_hash,password)
		
	def __repr__(self):
        return '<Employee: {}>'.format(self.username)	