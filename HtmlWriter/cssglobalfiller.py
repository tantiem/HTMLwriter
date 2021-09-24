file = input("What file do you want to apply globals to? ")
#Get a file name, probably a css file
#The idea behind this, is that in CSS, you mark certain sections to use variables for
#colors, fonts, and spacings.

#add this code to the top of your css file. It will separate on the equals, line by line, and use python
#find and replace to replace all variable values with it's equal. Needs to be in comments.
#i.e:
#/*
#accentcolor = #e9e9e9
#*/
#p {
#   color: [accentcolor];
#}:

#htmlbuildlib css globals:
#color1 = #abcdef
#fontstyle1 = Roboto
#paddingpreset1 = 0 10px

stylePage = open(file, 'r')
pageLines = stylePage.readlines()

newContent=""
styleVars = {}
inVars = True
for line in pageLines:
    curLine = str(line)
    if inVars:
        if "*/" in curLine:
            inVars = False
            break
        varAndValue = curLine.split("=")
        styleVars[varAndValue[0]] = varAndValue[1]
    else:
        for var in styleVars:
            curLine.replace(f'[{str(var).strip()}]',f'{styleVars[var].split()}')
            newContent += curLine

stylePage.close()


newFileName = file.replace('.css',"") + "varsub" + ".css"

newFile = open(newFileName,'w+')
newFile.write(newContent)
newFile.close()
print(newContent)
