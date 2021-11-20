from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, csrf
from wtforms.validators import DataRequired, Email

class MessageForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    message = TextAreaField("Message: ", validators=[DataRequired()])
    sumbit = SubmitField("Submit")
