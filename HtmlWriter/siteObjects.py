from htmlbuildlib import *

def header(bodyObj):

    menu2 = BaseXMLobj("h4", "", "About")
    menu3 = BaseXMLobj("h4", "", "Contact")
    menu4 = BaseXMLobj("h4","","Hi im extra!")
    list1 = BaseXMLobj("ul","","",[menu2,menu3,menu4])
    list2 = BaseXMLobj("ul","","",[list1])
    print(list2.returnXMLtag())
    bodyObj.addXMLobject(list2)