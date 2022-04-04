from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, BooleanField
from wtforms.validators import Length

class WebsiteForm(FlaskForm):
    image = FileField("image")
    fullName1 = StringField("Full name", validators=[Length(min=4, max=25)])
    firstSect1 = StringField("First Section", validators=[Length(min=4, max=25)])
    secondSect1 = StringField("Section Section", validators=[Length(min=4, max=25)])
    thirdSect1 = StringField("Third Section", validators=[Length(min=4, max=25)])
    fourthSect1 = StringField("Fourth Section", validators=[Length(min=4, max=25)])
    firstText1 = TextAreaField("First Text", validators=[Length(min=4)])
    secondText1 = TextAreaField("Second Text", validators=[Length(min=4)])
    thirdText1 = TextAreaField("Third Text", validators=[Length(min=4)])
    fourthText1 = TextAreaField("Fourth Text", validators=[Length(min=4)])
    submit = SubmitField("Generate Website")