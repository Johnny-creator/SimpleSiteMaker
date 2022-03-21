from flask import Flask, render_template, request, send_file
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results")
def results():
    f = open("webTemplates/simpleBox.txt", "r")
    webTemplate = f.read()

    fullName1 = request.args.get("fullName")
    firstSect1 =  request.args.get("firstSect")
    secondSect1 =  request.args.get("secondSect")
    thirdSect1 =  request.args.get("thirdSect")
    fourthSect1 =  request.args.get("fourthSect")
    firstText1 =  request.args.get("firstText")
    secondText1 =  request.args.get("secondText")
    thirdText1 =  request.args.get("thirdText")
    fourthText1 =  request.args.get("fourthText")

    webTemplate = webTemplate.format(fullName = fullName1, firstSect = firstSect1, secondSect = secondSect1, thirdSect = thirdSect1, fourthSect = fourthSect1, firstText = firstText1, secondText = secondText1, thirdText = thirdText1, fourthText = fourthText1)

    newWebsite = open("templates/tempSiteStorage/" + fullName1 + ".html", "w")
    newWebsite.write(webTemplate)
    newWebsite.close()
    

    # return render_template('tempSiteStorage/' + fullName1 + '.html')

    return send_file("templates/tempSiteStorage/" + fullName1 + ".html", as_attachment=True)

    # return render_template("results.html", testList = [fullName1, firstSect1, secondSect1, thirdSect1, fourthSect1, firstText1, secondText1, thirdText1, fourthText1])

if __name__ == "__main__":
    app.run(debug=True)