from flask_wtf import FlaskForm, Form
from flask_wtf.file import FileField
from wtforms import StringField, BooleanField, TextAreaField, SubmitField, validators, ValidationError
from wtforms.validators import DataRequired

class ContactForm(Form):
  name = StringField("Name",  [validators.Required()])
  email = StringField("Email",  [validators.Required(), validators.Email()])
  subject = StringField("Type of Project",  [validators.Required()])
  message = TextAreaField("Description",  [validators.Required()])
  submit = SubmitField("Send")

class CareerForm(FlaskForm):
  name = StringField("Name",  [validators.Required()])
  email = StringField("Email",  [validators.Required(), validators.Email()])
  file_r = FileField('Attach Resume', [validators.Required()])
  file_c = FileField('Attach or Copy and Paste Cover Letter')
  cover = TextAreaField("Letter")
  submit = SubmitField("Submit")