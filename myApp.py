from flask import Flask, render_template, request, send_file, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class WebsiteForm(FlaskForm):
    fullName1 = StringField("Full name", validators=[Length(min=4, max=25)])
    firstSect1 = StringField("First Section", validators=[Length(min=4, max=25)])
    secondSect1 = StringField("Section Section", validators=[Length(min=4, max=25)])
    thirdSect1 = StringField("Third Section", validators=[Length(min=4, max=25)])
    fourthSect1 = StringField("Fourth Section", validators=[Length(min=4, max=25)])
    firstText1 = TextAreaField("First Text", validators=[Length(min=4, max=25)])
    secondText1 = TextAreaField("Second Text", validators=[Length(min=4, max=25)])
    thirdText1 = TextAreaField("Third Text", validators=[Length(min=4, max=25)])
    fourthText1 = TextAreaField("Fourth Text", validators=[Length(min=4, max=25)])
    submit = SubmitField("Generate Website")


app = Flask(__name__)

app.config["SECRET_KEY"] = "superSecretKey"

fullNameHolder = ''

@app.route("/", methods=["GET", "POST"])
def index():
    form = WebsiteForm()

    if form.validate_on_submit():
        session["fullName1"] =  form.fullName1.data
        session["fullNameHolder"] = form.fullName1.data
        session["firstSect1"] = form.firstSect1.data
        session["secondSect1"] = form.secondSect1.data
        session["thirdSect1"] = form.thirdSect1.data
        session["fourthSect1"] = form.fourthSect1.data
        session["firstText1"] = form.firstText1.data
        session["secondText1"] = form.secondText1.data
        session["thirdText1"] = form.thirdText1.data
        session["fourthText1"] = form.fourthText1.data

        print("Ligma balls")

        return redirect(url_for("results"))
    
    return render_template("index.html", form=form)

@app.route("/results")
def results():
    f = open("webTemplates/simpleBox.txt", "r")
    webTemplate = f.read()

    webTemplate = webTemplate.format(fullName = session["fullName1"], firstSect = session["firstSect1"], secondSect = session["secondSect1"], thirdSect = session["thirdSect1"], fourthSect = session["fourthSect1"], firstText = session["firstText1"], secondText = session["secondText1"], thirdText = session["thirdText1"], fourthText = session["fourthText1"])

    newWebsite = open("templates/tempSiteStorage/" + session["fullName1"] + ".html", "w")
    newWebsite.write(webTemplate)
    newWebsite.close()

    return render_template("selection.html")

@app.route("/viewPage")
def viewPage():
    return render_template("tempSiteStorage/" + session["fullName1"] + ".html")
    

@app.route("/downloadPage")
def downloadPage():
    return send_file("templates/tempSiteStorage/" + session["fullName1"] + ".html", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)