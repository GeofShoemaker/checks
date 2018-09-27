from check50 import *


class Second(Checks):

    @check()
    def exists(self):
        """Demo exists"""
        self.require("Second.java")

    @check("exists")
    def compiles(self):
        """Divisible2 compiles""" 
        self.spawn("javac Second.java").exit(0)

    @check("compiles")
    def test1(self):
        """input of 3 correctly gives output of PRIME"""
        self.spawn("java Divisible2").stdin("3").stdout("PRIME\n", "PRIME\n")

    @check("compiles")
    def test2(self):
        """input of 12 correctly gives output of 2^2 * 3"""
        self.spawn("java Divisible2").stdin("12").stdout("2^2 * 3\n", "2^2 * 3\n")
