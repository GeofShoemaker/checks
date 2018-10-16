from check50 import *


class LibraryTester(Checks):

    @check()
    def exists(self):
        """LibraryTester.java exists"""
	self.require("LibraryTester.java")
#	self.require("Book.java")
#	self.require("Patron.java")
	
    @check()
    def compiles(self):
        """LibraryTester.java compiles"""
        self.spawn("javac LibraryTester.java").exit(0)

    @check()
    def test1(self):
        """Correctly Outputs"""
        self.spawn("java LibraryTester").stdout("true\n", "true\n").stdout("true\n", "true\n").stdout("false\n", "false\n").exit(0)
#My version

    
