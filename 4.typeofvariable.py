class car:
    wheel = 4#Class Variable(The Value common for all)
    def __init__(self,company,engine,mil):
        self.company= company#Instance Variable
        self.engine= engine
        self.mil= mil

c1 = car("BMW","V5",10)
c2 = car('Toyota','V8',9)
print(c1.company , c1.engine,c1.mil,c1.wheel)
print(c2.company , c2.engine,c2.mil,c2.wheel)
#There are two variable type in python OOP
#They are Intance Variable and Class Variable
