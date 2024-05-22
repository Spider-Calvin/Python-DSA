class Patterns:
    def __init__ (self, number):
        self.number = number

    def pattern1(self):
        n =  self.number
        print('pattern 1')
        
        num = 1
        for i in range(n):
            for j in range(i):
                print(num, end=' ')
                num+=1
            print()

    def pattern2(self):
        n =  self.number
        print('pattern 2')
        
        num = 65
        for i in range(n):
            for j in range(n-i):
                print(chr(num+i), end='')
            print()

    def pattern3(self):
        n =  self.number
        print('pattern 3')
        
        num = 65
        for i in range(n):
            for j in range(n-i):
                print(end=' ')
            for j in range((2*(i+1))-1):
                print( chr(num+i), end='')
            print()

    def pattern4(self):
        n =  self.number
        print('pattern 4')
        
        num = 65
        for i in range(n):
            v = 0
            for j in range(n-i):
                print(end=' ')
            for j in range(i+1):
                v+=1
                print( chr(num+j), end='')
            for j in range(i):
                print( chr(num+v-(j+2)), end='')
            print()

    def pattern5(self):
        n =  self.number
        print('pattern 5')
        
        num = 65+n
        for i in range(n):
            for j in range(i+1):
                print(chr(num-(i+1-j)),end='')
            print()


Pattern_instance = Patterns(6)

# Pattern_instance.pattern1()

# Pattern_instance.pattern2()

# Pattern_instance.pattern3()

# Pattern_instance.pattern4()

Pattern_instance.pattern5()

# Pattern_instance.pattern6()