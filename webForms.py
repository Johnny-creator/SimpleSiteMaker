from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, BooleanField
from wtforms.validators import Length

class pageCreationForm(FlaskForm):
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
    submit2 = SubmitField("Cancel")

class userLoginForm(FlaskForm):
    userName = StringField("User Name", validators=[Length(min=3, max=30)])
    passWord = StringField("Password", validators=[Length(min=5, max=50)])
    submit = SubmitField("Create User")