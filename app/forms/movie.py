from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms.validators import DataRequired, Length
from app.extensions import db

class MovieForm(FlaskForm):
    title = TextAreaField('',validators=[DataRequired(), Length(1,256)])



