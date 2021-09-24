from htmlbuildlib import buildSite

fileList = input("Give me yoru text file with a list of python site files!!!")

listFiles = open(fileList, 'r')
for file in listFiles:
    buildSite()

#work in progress


