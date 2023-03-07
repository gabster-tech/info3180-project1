from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired

class PropertyForm (FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    num_of_bedrooms = StringField('No. of Rooms',validators=[InputRequired()])
    num_of_bathrooms = StringField('No. of bathrooms',validators=[InputRequired()])
    location = StringField('Location',validators=[InputRequired()])
    price = StringField('Price',validators=[InputRequired()])
    type = SelectField('Property Type', choices=['House','Apartment'],validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['png','jpg'],'Images Only!')])