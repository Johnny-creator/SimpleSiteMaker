######################################
# THIS FILE WAS JUST USED FOR TESTING
######################################

if __name__ == "__main__":
    f = open("simpleBox.txt", "r")
    webTemplate = f.read()

    fullName1 = input("Please enter full Name: ")
    firstSect1 = input("Please enter first Sect: ")
    secondSect1 = input("Please enter second Sect: ")
    thirdSect1 = input("Please enter third Sect: ")
    fourthSect1 = input("Please enter fourth Sect: ")
    firstText1 = input("Please enter first Text: ")
    secondText1 = input("Please enter second Text: ")
    thirdText1 = input("Please enter third Text: ")
    fourthText1 = input("Please enter fourth Text: ")

    webTemplate = webTemplate.format(fullName = fullName1, firstSect = firstSect1, secondSect = secondSect1, thirdSect = thirdSect1, fourthSect = fourthSect1, firstText = firstText1, secondText = secondText1, thirdText = thirdText1, fourthText = fourthText1)
    
    newWebsite = open("newWebsite.html", "w")

    newWebsite.write(webTemplate)


    