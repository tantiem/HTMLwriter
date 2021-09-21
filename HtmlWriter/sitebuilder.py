from htmlbuildlib import *
head = Head()
body = Body()

h1 = makeTag("h1","","I am header 1 default piece")

head.setBasicMeta("Levi Reynolds", "My first htmlbuildlib site", "description", "viewport")
body.addXML(h1)
body.addXML(h1)
def double_para(para1,para2,bodyObj):
    bodyObj.addXML(makeTag("p","",para1))
    bodyObj.addXML(makeTag("p","",para2))


def header(bodyObj):

    menu2 = BaseXMLobj("h4", "", "About")
    menu3 = BaseXMLobj("h4", "", "Contact")
    list1 = BaseXMLobj("ul","","",[menu2,menu3])
    list2 = BaseXMLobj("ul","","",[list1])
    print(list2.returnXMLtag())
    bodyObj.addXMLobject(list2)

double_para("Bruh i am the first paragraph bro","Dog look at me im the second paragraph",body)
header(body)
buildSite(head, body, "index.html")
