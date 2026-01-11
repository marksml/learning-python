class C1(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello {self.name}")

c1 = C1("C1")
c1.hello()

