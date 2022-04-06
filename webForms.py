from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, PasswordField, ValidationError
from wtforms.validators import Length, DataRequired, EqualTo
from models import User

class pageCreationForm(FlaskForm):
    image = FileField("image", validators=[DataRequired()])
    fullName1 = StringField("Full name", validators=[Length(min=4, max=25), DataRequired()])
    firstSect1 = StringField("First Section", validators=[Length(min=4, max=25), DataRequired()])
    secondSect1 = StringField("Section Section", validators=[Length(min=4, max=25), DataRequired()])
    thirdSect1 = StringField("Third Section", validators=[Length(min=4, max=25), DataRequired()])
    fourthSect1 = StringField("Fourth Section", validators=[Length(min=4, max=25), DataRequired()])
    firstText1 = TextAreaField("First Text", validators=[Length(min=4), DataRequired()])
    secondText1 = TextAreaField("Second Text", validators=[Length(min=4), DataRequired()])
    thirdText1 = TextAreaField("Third Text", validators=[Length(min=4), DataRequired()])
    fourthText1 = TextAreaField("Fourth Text", validators=[Length(min=4), DataRequired()])
    submit = SubmitField("Generate Website")
    submit2 = SubmitField("Cancel")

class userLoginForm(FlaskForm):
    userName = StringField("User Name", validators=[DataRequired()])
    passWord = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class createUserForm(FlaskForm):
    userName = StringField("User Name", validators=[Length(min=3, max=30), DataRequired()])
    passWord = PasswordField("Password", validators=[Length(min=5, max=50), DataRequired(), EqualTo("confirmPassWord")])
    confirmPassWord = PasswordField("Password", validators=[Length(min=5, max=50), DataRequired()])
    submit = SubmitField("Create User")

    def validate_username(self, field):
        if User.query.filter_by(username=self.userName.data).first():
            raise ValidationError("Username is taken!")