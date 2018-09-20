import re

from check50 import *


class Cash(Checks):

    @check()
    def exists(self):
        """Cash exists"""
        self.require("Cash.java")

    @check("exists")
    def compiles(self):
        """Cash compiles"""
        self.spawn("javac Cash.java").exit(0)

    @check("compiles")
    def test041(self):
        """input of 0.41 yields output of 4"""
        self.spawn("java Cash").stdin("0.41").stdout(coins(4), "4\n").exit(0)

    @check("compiles")
    def test001(self):
        """input of 0.01 yields output of 1"""
        self.spawn("java Cash").stdin("0.01").stdout(coins(1), "1\n").exit(0)

    @check("compiles")
    def test015(self):
        """input of 0.15 yields output of 2"""
        self.spawn("java Cash").stdin("0.15").stdout(coins(2), "2\n").exit(0)

    @check("compiles")
    def test160(self):
        """input of 1.6 yields output of 7"""
        self.spawn("java Cash").stdin("1.6").stdout(coins(7), "7\n").exit(0)

    @check("compiles")
    def test230(self):
        """input of 23 yields output of 92"""
        self.spawn("java Cash").stdin("23").stdout(coins(92), "92\n").exit(0)

    @check("compiles")
    def test420(self):
        """input of 4.2 yields output of 18"""
        expected = "18\n"
        actual = self.spawn("java Cash").stdin("4.2").stdout()
        if not re.search(coins(18), actual):
            err = Error(Mismatch(expected, actual))
            if re.search(coins(22), actual):
                err.helpers = "Did you forget to round your input to the nearest cent?"
            raise err

    @check("compiles")
    def test_reject_negative(self):
        """rejects a negative input like -.1"""
        self.spawn("java Cash").stdin("-1").reject()

    @check("compiles")
    def test_reject_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("java Cash").stdin("").reject()


def coins(num):
    return r"(^|[^\d]){}(?!\d)".format(num)
