class Computer:
    def config(self):
        print('i5-3210M \n 4GB Ram \n 128GB SSD')

com1 = Computer()
com2 = Computer()
com1.config()
com2.config()
Computer.config(com1)
Computer.config(com2)
