from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,EmailField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    email=EmailField('Email')
    user_type=StringField('User Type',validators=[DataRequired()])
    approve_status=BooleanField('Approve Status')