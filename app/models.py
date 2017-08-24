#models for app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db,loginmanager

class student(UserMixin,db.Model):
    """create students table in database"""
    __tablename__='Students'
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(60),index=True)
    last_name=db.Column(db.String(60),index=True)
    email=db.Column(db.String(60),unique=True)
    phone=db.Column(db.Integer,index=True,unique=True)
    password_hash=db.Column(db.String(128))
    department_id=db.Column(db.Integer,db.ForeignKey('department.id'))
    course_unit_id=db.Column(db.Integer,db.ForeignKey('course_unit.id'))
    is_admin=db.Column(db.Boolean,default=True)
	
    @property
    def password(self):
        raise AttributeError('Password is not visible')
	   
    @password.setter
    def set_password(self,password):
        """sets password into a hashed password"""
        self.password_hash = generate_password_hash(password)	
		
	
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
		
    def __repr__(self):
        return '<student: {}>'.format(self.username)
    
@loginmanager.user_loader
def load_user(user_id):
        return student.query.get(int(user_id))	
		
class course_unit(db.Model):
    """create course unit table"""
    __tablename__='course_units'
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(250),index=True,unique=True)
    duration=db.Column(db.Integer,index=True)
    Students=db.relationship('student',backref='course_unit',
	                         lazy='dynamic')	
    def __repr__(self):
	    return '<course_unit:{}>'.format(self.name)
		
class department(db.Model):
    """create table for department"""
    __tablename__='Departments'
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(100),index=True,unique=True)
    description=db.Column(db.String(140))
    Students=db.relationship('student',backref='department',lazy='dynamic')
	
    def __repr__(self):
	    return '<department:{}>'.format(self.name)
	
	