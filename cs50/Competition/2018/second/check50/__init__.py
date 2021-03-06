from check50 import *


class Second(Checks):

    @check()
    def exists(self):
        """Demo exists"""
        self.require("Second.java")

    @check("exists")
    def compiles(self):
        """Second compiles""" 
        self.spawn("javac Second.java").exit(0)

    @check("compiles")
    def test1(self):
        """input of 1 0 0 100 100 0 correctly gives output of 1, 112\n"""
        self.spawn("java Second").stdin("1  0  0  100 100 0").stdout("1, 112\n", "1, 112\n\n")
