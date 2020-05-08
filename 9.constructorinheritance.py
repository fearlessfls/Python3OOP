class A:
    def __init__(self):
        print("This Is In init A")
    def fun1(self):
        print('This is fun 1 in class A')
    def fun3(self):
        print('Function 3 is working')
class B:
    def __init__(self):
        print('This is in init B')
    def fun1(self):
        print('This is fun1 in initB')
    def fun2(self):
        print('Function2 is working')
class C(B,A): #Left function came first #Super find the init of left super function
    def __init__(self):
        super().__init__()
        print('This is in init C')
    def function(self):
        super().fun3()
        
b1 = C()
b1.function()