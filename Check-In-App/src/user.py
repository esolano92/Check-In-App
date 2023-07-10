from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from  wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class User(FlaskForm):
    username = StringField("username: " ,validators=[DataRequired()])
    first_name = StringField("first name: ",validators=[DataRequired()])
    last_name = StringField("last name: ", validators=[DataRequired()])
    email = StringField("email: ",validators=[DataRequired()])
    password = PasswordField("pasword: ",validators=[DataRequired()])
    confirm_password = PasswordField("confrim password: ", validators=[DataRequired()])
    
    def __init__(self):
        self.create_user()
    
    def create_user(self, user_info=None):
        if user_info == None:
            user_info = {
                'username': self.username.data,
                'firstname': self.first_name.data,
                'lastname': self.last_name.data,
                'email': self.email.data,
                'password': self.password.data
                }
        return user_info
        
        