# inherit from the base class 'object' 
class Greeter(object):

    # definine an argument and a class variable initialized with the arguments
    def __init__(self,name):
        self.name = name

    def hello(self):
        print("Hello "+ self.name)

    def goodbye(self):
        print("Goodbye "+ self.name)

g = Greeter("Paul")
g.hello()
g.goodbye()
    
g2 = Greeter("Jessica")
g2.hello()
g2.goodbye()
    