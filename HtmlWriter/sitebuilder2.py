from htmlbuildlib import *
from siteObjects import *
#Add these at the begining of a site being made with htmlbuildlib. Gets the preset body and head objects.
head = Head()
body = Body()
#maketag is the function from htmlbuildlib. Unfavored to do this in childed elements, but works for single lines.
h1 = makeTag("h1","","I am header 1 default piece")
#set basic meta data, author, site title, site meta desc, and viewport lol
head.setBasicMeta("Levi Reynolds", "My first htmlbuildlib site", "description", "viewport")
#added my h1 from earlier to the body.
body.addXML(h1)
body.addXML(h1)



def double_para(para1,para2,bodyObj):
    bodyObj.addXML(makeTag("p","",para1))
    bodyObj.addXML(makeTag("p","",para2))


header(body)




double_para("Bruh i am the first paragraph bro","Dog look at me im the second paragraph",body)
header(body)
buildSite(head, body, "index2.html")
