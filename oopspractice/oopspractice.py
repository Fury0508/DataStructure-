class Samsung:
    def __init__(self):
        print("I am Samsung")

    def makeScreen(self):
        print("I make screens")
    
    def test(self):
        print("Screen test: OK")
#inhertiance
class Iphone(Samsung):
    def __init__(self):
        print("I am Iphone")
        # super().__init__()
    
    def a3chips(self):
        print("I make A3 bionic chips")
    
    def itest(self):
        print("A3 test: OK")
        # not a good practice
        #print("Screen test: OK")
        super().test()
    
    def makeScreen(self):
        print("I make screens: Apple")

user = Iphone()

user.a3chips()
user.makeScreen()
user.itest()
        