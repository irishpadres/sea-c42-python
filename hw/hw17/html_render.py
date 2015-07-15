#!/usr/bin/env python

"""
Python class example.

"""


# The start of it all:
# Fill it all in here.
class Element(object):

    BASE_INDENT = "    "

    def __init__(self, tag="", content=None, oneLineFlag=False, **kwargs):
        self.tag = tag
        self.content = []
        self.append(content)
        self.oneLineFlag = oneLineFlag
        self.attrs = []
        self.attrStr = ''
        if (kwargs is not None):
            for key, val in kwargs.items():
                self.attrs.append("%s=\"%s\"" % (key, val))
        if (len(self.attrs) > 0):
            self.attrStr = " " + " ".join(self.attrs)

    def append(self, content):
        if (content):
            self.content.append(content)

    def render(self, fh, indent=""):
        fh.write("%s<%s%s>" % (indent, self.tag, self.attrStr))
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

    def __init__(self, content="", **kwargs):
        Element.__init__(self, tag="html", content=content, oneLineFlag=False, **kwargs)

    def render(self, fh, indent=""):
        fh.write("<!DOCTYPE html>\n")
        Element.render(self, fh)


class Body(Element):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, tag="body", content=content, oneLineFlag=False, **kwargs)


class P(Element):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, tag="p", content=content, oneLineFlag=False, **kwargs)


class Head(Element):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, tag="head", content=content, oneLineFlag=False, **kwargs)


class OneLineTag(Element):

    def __init__(self, tag="", content="", **kwargs):
        Element.__init__(self, tag=tag, content=content, oneLineFlag=True, **kwargs)


class Title(OneLineTag):

    def __init__(self, content="", **kwargs):
        OneLineTag.__init__(self, tag="title", content=content, **kwargs)
