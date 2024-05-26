class Patterns:
    def __init__ (self, number):
        self.number = number

    def pattern1 (self):
        n = self.number

        for i in range(n):
            for j in range(n):
                print('*', end='')
            print()

    def pattern2 (self):
        n = self.number

        for i in range(n):
            for j in range(i+1):
                print('*', end='')
            print()
            
    def pattern3 (self):
        n = self.number

        for i in range(n):
            for j in range(i+1):
                print(i+1, end='')
            print()

    def pattern4 (self):
        n = self.number

        for i in range(n):
            for j in range(i+1):
                print(i+1, end='')
            print()

    def pattern5 (self):
        n = self.number

        for i in range(n):
            for j in range(n-i):
                print('*', end='')
            print()

    def pattern6 (self):
        n = self.number

        for i in range(n):
            for j in range(n-i):
                print(j+1, end='')
            print()

    def pattern7 (self):
        n = self.number

        for i in range(n):
            i+=1
            for j in range(n-i):
                print(end=' ')

            for j in range((2*i)-1):
                print('*', end='')
            print()

    def pattern8 (self):
        n = self.number

        for i in range(n):
            for j in range(i):
                print(end=' ')

            for j in range((2*(n-i))-1):
                print('*', end='')
            print()

    def pattern9 (self):
        n = self.number

        for i in range(2*n):
            if(i<n):
                i+=1
                for j in range(n-i):
                    print(end=' ')

                for j in range((2*i)-1):
                    print('*', end='')
                print()
            else:
                m=i-n
                for i in range (m):
                     print(end=' ')
                for j in range ((2*(n-m))-1):
                     print('*', end='')
                print()
    
    def pattern10 (self):
        n = self.number

        for i in range(2*n):
            if(i<n):
                i+=1
                for j in range(i):
                    print('*', end='')
                print()
            else:
                x = i-n+1
                for j in range(n-x):
                    print('*', end='')
                print()
    
    def pattern11 (self):
        n = self.number

        for i in range(n):
            for j in range(i+1):
                j+=1
                print(j%2, end='')
            print()

    def pattern12 (self):
        n = self.number
        for i in range(n):
            i+=1
            for j in range(i):
                print(j+1, end='')
            for j in range((2*n-2*i)):
                print(end=' ')
            for j in range(i, 0, -1):
                print(j, end='')
            print()
    
    def pattern13 (self):
        n = self.number
        x=1
        for i in range(n):
            for j in range(i+1):
                print(x, end=' ')
                x+=1
            print()
    
    def pattern14 (self):
        n = self.number
        char_code = ord('A')
        
        for i in range(n):
            for j in range(i+1):
                print(chr(char_code), end=' ')
                char_code+=1
            print()
    
    def pattern15(self):
        n = self.number
        char_code =ord('A')

        for i in range(n):
            for j in range(n-i):
                print(chr(char_code+j), end=' ')
            print()

    def pattern16 (self):
        n= self.number
        char_code=ord('A')

        for i in range(n):
            for j in range(i+1):
                print(chr(char_code), end=' ')
            char_code+=1
            print()
    
    def pattern17 (self):
        n=self.number
        

        for i in range(n):
            i+=1
            char_code=ord('A')
            gap=0

            for j in range(n-i):
                print(end=' ')

            for j in range(i):
                print(chr(char_code), end='')
                char_code+=1
                gap+=1

            for j in range(gap-1):
                print(chr(char_code-2), end='')
                char_code-=1

            print()

    def pattern18(self):
        n=self.number
        char_code=ord('A')+n

        for i in range(n):
            for j in range(i+1,0,-1):
                print(chr(char_code-j), end=' ')
            print()
    
    def pattern18(self):
        n=self.number
        char_code=ord('A')+n-1

        for i in range(n):
            for j in range(i+1):
                rev = i-j
                print(chr(char_code-rev), end=' ')
            print()

    def pattern19(self):
        n=self.number

        for i in range(2*n):
            if(i<n):
                for x in range(n-i):
                    print(x+1,end='')

                for x in range(2*i):
                    print(end=' ')
                
                for x in range(n-i,0,-1):
                    print(x, end='')
            else:
                k=i-n+1
                for x in range(k):
                    print(x+1,end='')

                for x in range(2*n-2*k):
                    print(end=' ')
                
                for x in range(k):
                    print(x+1,end='')
            print()

    def pattern20(self):
        n=self.number

        for i in range(2*n-1):
            if(i<n):
                for j in range(i+1):
                    print('*', end='')
                for j in range(2*n-2*(i+1)):
                    print(end=' ')
                for j in range(i+1):
                    print('*', end='')
                print()
            else:
                k=i-n+1
                for j in range(n-k):
                    print('*',end='')
                for j in range(2*k):
                    print(end=' ')
                for j in range(n-k):
                    print('*',end='')
                print()

    def pattern21(self):
        n=self.number
        for i in range(n):
            for j in range(n):
                if(i==0 or j==0 or i==n-1 or j==n-1 ):
                    print('*', end='')
                else:
                    print(' ', end='')
            print('')

    def pattern22(self):
        n=self.number

        for i in range(2*n-1):
            for j in range(2*n-1):
                a=i
                b=j
                c=(2*n)-2-i
                d=(2*n)-2-j
                x = min(min(a, b), min(c, d))
                print(x, end=' ')
            print()

    def pattern22(self):
        n=self.number

        for i in range(2*n-1):
            for j in range(2*n-1):
                a=i
                b=j
                c=(2*n)-i-2
                d=(2*n)-j-2
                x = min(min(a, b), min(c, d))
                print(n-x, end=' ')
            print()


patternInstance = Patterns(5)


# patternInstance.pattern1()
# patternInstance.pattern2()
# patternInstance.pattern3()
# patternInstance.pattern4()
# patternInstance.pattern5()
# patternInstance.pattern6()
# patternInstance.pattern7()
# patternInstance.pattern8()
# patternInstance.pattern9()
# patternInstance.pattern10()
# patternInstance.pattern11()
# patternInstance.pattern12()
# patternInstance.pattern13()
# patternInstance.pattern14()
# patternInstance.pattern15()
# patternInstance.pattern16()
# patternInstance.pattern17()
# patternInstance.pattern18()
# patternInstance.pattern19()
# patternInstance.pattern20()
# patternInstance.pattern21()
# patternInstance.pattern22()