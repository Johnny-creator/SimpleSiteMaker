import os
import shutil
from os.path import basename
from flask import Flask, render_template, request, send_file, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, TextAreaField, FileField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_uploads import configure_uploads, IMAGES, UploadSet
from zipfile import ZipFile


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


app = Flask(__name__)

app.config["SECRET_KEY"] = "superSecretKey"
app.config["UPLOADED_IMAGES_DEST"] = "userImages"

images = UploadSet("images", IMAGES)
configure_uploads(app, images)

@app.route("/", methods=["GET", "POST"])
def index():
    nameNoSpace = ""
    form = WebsiteForm()

    if form.validate_on_submit():
        session["fullName1"] =  form.fullName1.data
        session["firstSect1"] = form.firstSect1.data
        session["secondSect1"] = form.secondSect1.data
        session["thirdSect1"] = form.thirdSect1.data
        session["fourthSect1"] = form.fourthSect1.data
        session["firstText1"] = form.firstText1.data
        session["secondText1"] = form.secondText1.data
        session["thirdText1"] = form.thirdText1.data
        session["fourthText1"] = form.fourthText1.data

        # Replace all spaces in the users first name
        nameNoSpace = session["fullName1"].replace(" ", "")

        # Make directory for the users website
        try:
            os.mkdir("templates/tempSiteStorage/" + session["fullName1"].replace(" ", ""))
        except:
            shutil.rmtree("templates/tempSiteStorage/" + session["fullName1"].replace(" ", ""))
            os.mkdir("templates/tempSiteStorage/" + session["fullName1"].replace(" ", ""))

        # Save the image from the form to a temporary directory
        images.save(form.image.data, name="userImage.jpg")

        # Move the image to the users directory
        src_path = r"userImages/userImage.jpg"
        dst_path = r"templates/tempSiteStorage/" + session["fullName1"].replace(" ", "")
        shutil.move(src_path, dst_path)

        return redirect(url_for("results"))
    
    return render_template("index.html", form=form)

@app.route("/results")
def results():
    f = open("webTemplates/simpleBox.txt", "r")
    webTemplate = f.read()

    webTemplate = webTemplate.format(fullName = session["fullName1"], firstSect = session["firstSect1"], secondSect = session["secondSect1"], thirdSect = session["thirdSect1"], fourthSect = session["fourthSect1"], firstText = session["firstText1"], secondText = session["secondText1"], thirdText = session["thirdText1"], fourthText = session["fourthText1"])

    newWebsite = open("templates/tempSiteStorage/" + session["fullName1"].replace(" ", "") + "/index.html", "w")
    newWebsite.write(webTemplate)
    newWebsite.close()

    return render_template("selection.html")

@app.route("/viewPage")
def viewPage():
    return render_template("tempSiteStorage/" + session["fullName1"].replace(" ", "") + "/index.html")
    # return render_template("tempSiteStorage/test.html")
    

@app.route("/downloadPage")
def downloadPage():
    try:
        with ZipFile(session["fullName1"].replace(" ", "") + ".zip", "w") as zipSite:
            for folderName, subfolders, filenames in os.walk("templates\\tempSiteStorage\\" + session["fullName1"].replace(" ", "")):
                for filename in filenames:
                    filePath = os.path.join(folderName, filename)
                    zipSite.write(filePath, basename(filePath))
    except:
        # Remove original file
        os.remove(session["fullName1"].replace(" ", "") + ".zip")

    return send_file(session["fullName1"].replace(" ", "") + ".zip", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)