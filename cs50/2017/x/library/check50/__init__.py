from check50 import *


class LibraryTester(Checks):

    @check()
    def exists(self):
        """LibraryTester.java exists"""
	self.require("LibraryTester.java")
#	self.require("Book.java")
#	self.require("Patron.java")
	
    @check("exists")
    def compiles(self):
        """LibraryTester.java compiles"""
        self.spawn("javac LibraryTester.java").exit(0)

    @check("compiles")
    def test1(self):
        """Correctly Outputs"""
        self.spawn("java LibraryTester").stdout("true\n", "true\n")).exit(0)
        self.spawn("java LibraryTester").stdout("true\n", "true\n")).exit(0)
        self.spawn("java LibraryTester").stdout("true\n", "true\n")).exit(0)
#My version

    
