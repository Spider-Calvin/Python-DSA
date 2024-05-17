class Patterns:
    def __init__ (self, number):
        self.number = number

    def pattern1(self):
        n =  self.number
        print('pattern 1')

        for i in range(n):
            for j in range(n-(i+1)):
                print(end=' ')

            for j in range(2*(i+1)-1):
                print("*", end='')
            print()
        print()
    
    def pattern2(self):
        n =  self.number
        print('pattern 2')

        for i in range(n):
            for j in range(i):
                print(end=' ')

            for j in range(2*(n-i)-1):
                print("*", end='')
            print()
        print()

    def pattern3(self):
        n =  self.number
        print('pattern 3')

        for i in range(n):
            for j in range(n-(i+1)):
                print(" ", end='')

            for j in range(2*(i+1)-1):
                print("*", end='')
            print()
        print()

    def pattern4(self):
        n =  self.number
        print('pattern 4')

        for i in range((2*n)+1):
            if i < n:
                for j in range(i+1):
                    print("*", end='')
            else:
                for j in range((2*n)-(i+1)):
                    print("*", end='')
            print()
        print()
    
    def pattern5(self):
        n =  self.number
        print('pattern 5')

        for i in range((2*n)+1):
            if i < n:
                for j in range(n-(i+1)):
                    print(end=' ')
                for j in range(i+1):
                    print(end='*')
            else:
                for j in range(n-(2*n-(i+1))):
                    print(end=' ')
                for j in range((2*n)-(i+1)):
                    print("*", end='')
            print()
        print()


Pattern_instance = Patterns(5)

Pattern_instance.pattern1()

Pattern_instance.pattern2()

Pattern_instance.pattern3()

Pattern_instance.pattern4()

Pattern_instance.pattern5()

# Pattern_instance.pattern6()