import os
import shutil
from os.path import basename


from flask_uploads import configure_uploads, IMAGES, UploadSet
from zipfile import ZipFile


from SimpleSiteProject import app, db, images
from flask import render_template, request, send_file, session, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from SimpleSiteProject.models import User
from SimpleSiteProject.webForms import createUserForm, pageCreationForm, userLoginForm
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/pageCreator", methods=["GET", "POST"])
def pageCreator():
    nameNoSpace = ""
    form = pageCreationForm()

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

        # Make directory for the users website
        try:
            os.mkdir("SimpleSiteProject/templates/tempSiteStorage/" + session["fullName1"].replace(" ", ""))
        except:
            shutil.rmtree("SimpleSiteProject/templates/tempSiteStorage/" + session["fullName1"].replace(" ", ""))
            os.mkdir("SimpleSiteProject/templates/tempSiteStorage/" + session["fullName1"].replace(" ", ""))

        # Save the image from the form to a temporary directory
        images.save(form.image.data, name="userImage.jpg")

        # Move the image to the users directory
        src_path = r"userImages/userImage.jpg"
        dst_path = r"SimpleSiteProject/templates/tempSiteStorage/" + session["fullName1"].replace(" ", "")
        shutil.move(src_path, dst_path)

        # Create index.html
        f = open("webTemplates/simpleBox.txt", "r")
        webTemplate = f.read()

        webTemplate = webTemplate.format(fullName = session["fullName1"], firstSect = session["firstSect1"], secondSect = session["secondSect1"], thirdSect = session["thirdSect1"], fourthSect = session["fourthSect1"], firstText = session["firstText1"], secondText = session["secondText1"], thirdText = session["thirdText1"], fourthText = session["fourthText1"])

        newWebsite = open("SimpleSiteProject/templates/tempSiteStorage/" + session["fullName1"].replace(" ", "") + "/index.html", "w")
        newWebsite.write(webTemplate)
        newWebsite.close()

        if current_user.is_authenticated:
            os.chdir("SimpleSiteProject/siteStorage/" + str(current_user.id) + "-sites" )
            
            try:
                with ZipFile(session["fullName1"].replace(" ", "") + ".zip", "w") as zipSite:
                    for folderName, subfolders, filenames in os.walk("/home/admin/SimpleSiteMaker/SimpleSiteProject/templates/tempSiteStorage/" + session["fullName1"].replace(" ", "")):
                        print(os.getcwd())
                        for filename in filenames:
                            filePath = os.path.join(folderName, filename)                            
                            zipSite.write(filePath, basename(filePath))
            except:
                # Remove original file
                os.remove("../" + session["fullName1"].replace(" ", "") + ".zip")

            # Reset Directory
            os.chdir("../../..")
            

        return redirect(url_for("results"))
    
    return render_template("pageCreator.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('index'))

@app.route("/results")
def results():

    return render_template("selection.html")

@app.route("/viewPage")
def viewPage():
    return render_template("tempSiteStorage/" + session["fullName1"].replace(" ", "") + "/index.html")

@app.route("/userLogin", methods=["GET", "POST"])
def userLogin():

    form = userLoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(username=form.userName.data).first()

        # Check that the user was supplied and the password is right
        if  user is not None and user.check_password(form.passWord.data):
            # Log in the user
            login_user(user)
            flash("Logged in successfully")

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('index')

            return redirect(next)
    return render_template("userLogin.html", form=form)

@app.route("/createUser", methods=["GET", "POST"])
def createUser():
    form = createUserForm()

    if form.validate_on_submit():
        user = User(username=form.userName.data,
                    password=form.passWord.data)

        db.session.add(user)
        db.session.commit()

        os.chdir("SimpleSiteProject/siteStorage")
        os.mkdir(user.get_id() + "-sites")
        os.chdir("../..")
        print(os.listdir())

        flash("Thanks for registering!")
        return redirect(url_for("userLogin"))
    return render_template("createUser.html", form=form)

@app.route("/downloadPage")
def downloadPage():
    try:
        with ZipFile(session["fullName1"].replace(" ", "") + ".zip", "w") as zipSite:
            for folderName, subfolders, filenames in os.walk("SimpleSiteProject/templates/tempSiteStorage/" + session["fullName1"].replace(" ", "")):
                for filename in filenames:
                    filePath = os.path.join(folderName, filename)
                    zipSite.write(filePath, basename(filePath))
    except:
        # Remove original file
        os.remove("../" + session["fullName1"].replace(" ", "") + ".zip")

    return send_file("../" + session["fullName1"].replace(" ", "") + ".zip", as_attachment=True)


@app.route("/userFiles")
def userFiles():
    dirPath = "/home/admin/SimpleSiteMaker/SimpleSiteProject/siteStorage/" + str(current_user.id) + "-sites"
    files = os.listdir(dirPath)

    return render_template("userFiles.html", path=dirPath, files=files)

@app.route("/userDownload/<selectedFile>")
def userDownload(selectedFile):
    dirPath = "/home/admin/SimpleSiteMaker/SimpleSiteProject/siteStorage/" + str(current_user.id) + "-sites/"
    
    file = selectedFile
    return send_file(dirPath + file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)