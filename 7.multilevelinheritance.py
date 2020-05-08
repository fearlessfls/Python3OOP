class A:
    def function1(self):
        print('Function 1 is working')
    def function2(self):
        print('Function 2 is working')
class B(A):
    def function3(self):
        print('Function 3 is working')
    def function4(self):
        print('Function 4 is working')
class C(B):
    def function5(self):
        print('Function 5 is working')
    def function6(self):
        print('Function 6 is working')

c = C()
c.function1()
c.function2()