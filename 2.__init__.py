class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Config is {} CPU and {} RAM'.format(self.cpu,self.ram))

com1 = computer('i5-3210M','4GB')
com2 = computer('i5-4400U','8GB')
com1.config()
com2.config()
