class Patterns:
    def __init__ (self, number):
        self.number = number

    def pattern1(self):
        n =  self.number
        print('pattern 1')

        for i in range(n):
            for j in range(n):
                print("*", end='')
            print()

        print()


Pattern_instance = Patterns(5)

# Pattern_instance.pattern1()

# Pattern_instance.pattern2()

# Pattern_instance.pattern3()

# Pattern_instance.pattern4()

# Pattern_instance.pattern5()

# Pattern_instance.pattern6()