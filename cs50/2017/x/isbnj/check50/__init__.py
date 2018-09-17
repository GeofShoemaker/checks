from check50 import *


class ISBN(Checks):
    
    @check()
    def exists(self):
        """ISBN.java exists."""
        self.require("ISBN.java")
    
    @check("exists")
    def compiles(self):
        """ISBN.java compiles."""
        self.spawn("javac ISBN.java").exit(0)
    
   
    @check("compiles")
    def Absolute_Beginners_Guide(self):
        """Beginners Guide (0789751984) valid"""
        self.spawn("java ISBN").stdin("0789751984").stdout("^YES\n", "YES\n").exit(0)

    @check("compiles")
    def Absolute_Beginners_Guide_fake(self):
        """Beginners Guide fake (0789751985) invalid"""
        self.spawn("java ISBN").stdin("0789751985").stdout("^NO\n", "NO\n").exit(0)

    @check("compiles")
    def Programming_in_C(self):
        """Programming in C (0321776410) valid"""
        self.spawn("java ISBN").stdin("0321776410").stdout("^YES\n", "YES\n").exit(0)

    @check("compiles")
    def Hackers_Delight(self):
        """Hackers Delight (0321842685) valid"""
        self.spawn("java ISBN").stdin("0321842685").stdout("^YES\n", "YES\n").exit(0)

    @check("compiles")
    def phone_number(self):
        """Jennys number (6178675309) invalid"""
        self.spawn("java ISBN").stdin("6178675309").stdout("^NO\n", "NO\n").exit(0)

    @check("compiles")
    def memory(self):
        """Mystery Test"""
        self.spawn("java ISBN").stdin("1632168146").stdout("^YES\n", "YES\n").exit(0)

    @check("compiles")
    def ISBN_with_X(self):
        """rejects ISBNs with X as checksum"""
        self.spawn("java ISBN").stdin("078974984X").stdout("^Error!\n", "Error!\n").exit(0)
    @check("compiles")
    def rejects_ISBNs_with_dashes(self):
        """rejects ISBNs with dashes"""
        self.spawn("java ISBN").stdin("0-789-75198-4").stdout("^Error!\n", "Error!\n").exit(0)

    @check("compiles")
    def rejects_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("java ISBN").stdin("").reject()
