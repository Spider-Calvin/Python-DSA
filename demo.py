class Patterns:
    def __init__ (self, number):
        self.number = number

    def pattern1(self):
        n =  self.number

        for i in range(n):
            for j in range(n):
                print("*", end='')
            print()
    
    def pattern2(self):
        n =  self.number

        for i in range(n):
            for j in range(i):
                print("*", end='')
            print()

Pattern_instance = Patterns(5)

Pattern_instance.pattern1()

Pattern_instance.pattern2()