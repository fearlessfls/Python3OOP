class info:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
p1 = info("Kaung Kaung" , 18)
p2 = info("Kyaw Gyi" , 19)

if p1.compare(p2):
    print('They are Same age')
else:
    print('They are Different age')
