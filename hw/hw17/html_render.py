#!/usr/bin/env python

"""
Python class example.

"""


# The start of it all:
# Fill it all in here.
class Element(object):

    BASE_INDENT = "    "

    def __init__(self, tag="", content=None):
        self.tag = tag
        self.content = []
        self.append(content)

    def append(self, content):
        if (content):
            self.content.append(content)

    def render(self, fh, indent=""):
        fh.write("%s<%s>\n" % (indent, self.tag))
        curIndent = indent + Element.BASE_INDENT
        for content in self.content:
            if (isinstance(content, str)):
                fh.write("%s%s\n" % (curIndent, content))
            elif (isinstance(content, Element)):
                content.render(fh, curIndent)
        fh.write("%s</%s>\n" % (indent, self.tag))


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
