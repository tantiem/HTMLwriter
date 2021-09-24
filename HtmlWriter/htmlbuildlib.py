#MIT License

#Copyright (c) 2021 Levi Reynolds

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
#---------------------------------------------------------------------------

#INTRODUCTION
#This is a library dedicated to the simplification of the html site building process. I always find the most irritating
#part of making a website is how often you have to repeat yourself, and how hard it is to make changes in a big site.
#Therefore, this library was made as a sort of higher level parser to allow for the creation, reuse, and mutability
#of XML objects for html in the same way that the react library does, but without the need for a server or server sided
#language. Simple and to the point, this is a way to write reusable HTML in easy to read and parse python.
#-----------------------------------------------------------------------------------------------------------


#There are two ways to make general tags:
#  A simple text tag,
#  or an object tag.
#An object tag is made by creating an instance of the BaseXMLobj class. It takes a tag, props, content, and optional
#children. I would reccomend not messing with the base indent param. It is defaulted as to not be needed to change,
#but inside of this library is used extensivley in recursively determining the spacing from the left in order to make
#the generated code readable and editable.

#Globals for base document
#Globals cover a wide range of possible site wide colors, fonts, or even text gen settings.
gBaseIndent = 2

#A base functional class for all other custom classes to inherit
#The order for all object making is tag, props, content, children
#You may make a class that inherits from BaseXMLobj. In fact, its a large point of functionality of the library.
class BaseXMLobj:
    def __init__(self, tag="", props="", content="",children=[],indent=gBaseIndent):
        self.content = content
        self.tag = tag
        self.children = children
        self.props = props
        self.indent = indent
        if len(children) > 0:
            #If there are children in the children list, add them all to my content before adding my closing tags.
            #This recurses, so that the text structure remains readable and functional.
            childContent = ""
            for i in range(len(children)):
                curChild = children[i]
                try:
                    childContent += makeTag(curChild.tag, curChild.props, curChild.content, curChild.children, self.indent + gBaseIndent)
                except AttributeError:
                    #The child does not inherit from BaseXMLObj
                    childContent += children[i]
                childContent += ""
            self.content += childContent

    def returnContent(self):
        return self.content

    def returnXMLtag(self):
        if self.tag != "":
            return makeTag(self.tag,self.props,self.content,self.children,self.indent)
        else:
            print("Could not utilize returnXMLtag on a BaseXMLobj: Missing tag!")


#Functionally everything relating to the head section of the document contained
#in this object. It is streamlined to allow for the most common meta tags, and addition thereof.
class Head(BaseXMLobj):
    def __init__(self):
        super().__init__()
        self.content = ""

    def setBasicMeta(self, author, title, description, viewport):
        content = f"<meta name=\"description\" content=\"{description}\">\n"
        content += f"<meta name=\"author\" content=\"{author}\">\n"
        content += makeTag("title","",f"{title}")
        self.content += content



#Functionally everything relating to the body section of the document contained
#in this object
#addXMLobject adds a tag object to the body.
#addXML adds a text tag to the body.
class Body(BaseXMLobj):
    def __init__(self):
        super().__init__()
        self.content = ""
        self.scriptRefs = ""

    def returnContent(self):
        return self.content + "\n" + self.scriptRefs

    def addXMLobject(self, obj):
        self.content += f"{obj.returnContent()}"

    def addXML(self,xml):
        self.content += f"{xml}\n"


#content is text. tag is the xml tag, i.e. h1 or p in plain text. props are same as in html,
#i.e class="myclass", quotes and all. children is a list of type xml object, this supports recursive childing.
#supporting the two methods of xml object creation, makeTag can work with a mix of simple text tags and class tags.

#it is NOT ADVISED to use this for deep childing elements. It is useful to get a quick one off on some tags with simple
#Hierarchies, but you will have to manage indentation yourself or else the code afterwards will look like a mess.
#Functionally, there are no downsides to doing this however.
def makeTag(tag,props,content,children=[], indent=0):
    curindent = indent
    spacing = " " * curindent
    prevSpacing = " " * (curindent - gBaseIndent)
    if len(children) > 0:
        childContent=""
        for i in range(len(children)):
            curChild = children[i]
            try:
                childContent += makeTag(curChild.tag, curChild.props, curChild.content, curChild.children, curindent+gBaseIndent)
            except AttributeError:
                childContent += children[i]
            childContent += ""
        return f"{spacing}<{tag} {props}>\n{childContent}\n{prevSpacing}</{tag}>"
    else:
        contentSpacing = spacing + (" "*gBaseIndent)
        return f"{spacing}<{tag} {props}>\n{contentSpacing}{content}\n{spacing}</{tag}>\n"

##Edit if you want to. This is your structure of site body.
def buildSite(head,body,file):
    file = open(file, "w+")
    file.write("<!DOCTYPE html>\n")
    file.write("<html>\n")
    file.write("  <head>\n")
    file.write(head.returnContent())
    file.write("  </head>\n")
    file.write("  <body>\n")
    file.write(body.returnContent())
    file.write("   </body>\n")
    file.write("</html>\n")
    file.close()







