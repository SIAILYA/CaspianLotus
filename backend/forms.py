from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, csrf, FileField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired


class MessageForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    message = TextAreaField("Message: ", validators=[DataRequired()])
    sumbit = SubmitField("Submit")

class AddReviewForm(FlaskForm):
    name = StringField("Имя: ", validators=[DataRequired()])
    review = TextAreaField("Отзыв: ", validators=[DataRequired()])
    submit = SubmitField("Подтвердить")

class EditReviewForm(FlaskForm):
    name = StringField("Имя: ", validators=[DataRequired()])
    review = TextAreaField("Отзыв: ", validators=[DataRequired()])
    submit = SubmitField("Подтвердить")

class EditPriceForm(FlaskForm):
    name = StringField("Имя: ", validators=[DataRequired()])
    count = TextAreaField("Цена: ", validators=[DataRequired()])
    submit = SubmitField("Подтвердить")

class AddPhotoForm(FlaskForm):
    photo = FileField( u'pictures',
    validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField("Подтвердить")

