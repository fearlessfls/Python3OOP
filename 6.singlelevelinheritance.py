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

b1 = B()
b1.function1()
b1.function2()