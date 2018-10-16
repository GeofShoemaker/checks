from check50 import *


class LibraryTester(Checks):

    @check()
    def exists(self):
        """Library/Book.java"""
	self.require("Book.java")
	"""Library/Patron.java"""
	self.require("Patron.java")
	"""Library/LibraryTester.java"""
	self.require("LibraryTester.java")
	
	
    @check()
    def compiles(self):
        """LibraryTester.java compiles"""
        self.spawn("javac LibraryTester.java Book.java Patron.java").exit(0)

    @check("compiles")
    def test1(self):
        """Correctly Outputs"""
        self.spawn("java LibraryTester").stdout("true\ntrue\ntrue\nfalse\n", "true\ntrue\ntrue\nfalse\n").exit(0)
