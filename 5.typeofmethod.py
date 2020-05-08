class student:
    school = 'B.E.H.S(3)Bago'
    def __init__(self,name,chem,phys):
        self.name = name
        self.chem = chem
        self.phys = phys
    def avg(self):
        return (self.chem+self.phys)/2
    @classmethod
    def get_schoolname(cls):
        return student.school
    @staticmethod
    def classroom():
        return 'Class D'
s1 = student("Mg Mg" , 80 , 90)
s2 = student("Ko KO" , 70 , 100)
print(f'These are avg exam marks of {student.get_schoolname()} From {student.classroom()}')
print(f'{s1.name} get avg {s1.avg()} marks')
print(f'{s2.name} get avg {s2.avg()} marks')
