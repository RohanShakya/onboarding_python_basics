class Person:
    def __init__(self):
        self.name = ""

    def getString(self):
        self.name = input("Enter your name: ")

    def printString(self):
        print(self.name.upper())


p1 = Person()
p1.getString()
p1.printString()

