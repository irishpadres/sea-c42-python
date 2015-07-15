#!/usr/bin/env python

"""
Python class example.

"""


# The start of it all:
# Fill it all in here.
class Element(object):

    BASE_INDENT = "    "

    def __init__(self, tag="", content=None, oneLineFlag=False):
        self.tag = tag
        self.content = []
        self.append(content)
        self.oneLineFlag = oneLineFlag

    def append(self, content):
        if (content):
            self.content.append(content)

    def render(self, fh, indent=""):
        fh.write("%s<%s>" % (indent, self.tag))
        if not self.oneLineFlag:
            fh.write("\n")
        curIndent = indent + Element.BASE_INDENT
        for content in self.content:
            if (isinstance(content, str)):
                if self.oneLineFlag:
                    fh.write("%s" % (content))
                else:
                    fh.write("%s%s\n" % (curIndent, content))
            elif (isinstance(content, Element)):
                content.render(fh, curIndent)
        if not self.oneLineFlag:
            fh.write("%s" % (indent))
        fh.write("</%s>\n" % (self.tag))


class Html(Element):

    def __init__(self, content=""):
        Element.__init__(self, tag="html", content=content)

    def render(self, fh, indent=""):
        fh.write("<!DOCTYPE html>\n")
        Element.render(self, fh)


class Body(Element):

    def __init__(self, content=""):
        Element.__init__(self, tag="body", content=content)


class P(Element):

    def __init__(self, content=""):
        Element.__init__(self, tag="p", content=content)


class Head(Element):

    def __init__(self, content=""):
        Element.__init__(self, tag="head", content=content)


class OneLineTag(Element):

    def __init__(self, tag="", content=""):
        Element.__init__(self, tag=tag, content=content, oneLineFlag=True)


class Title(OneLineTag):

    def __init__(self, content=""):
        OneLineTag.__init__(self, tag="title", content=content)
