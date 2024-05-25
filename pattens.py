class Patterns:
    def __init__ (self, number):
        self.number = number

    def printNum (self, x):
        print(self.number,x)

patternInstance = Patterns(5)

patternInstance.printNum('hello my lovely lady')