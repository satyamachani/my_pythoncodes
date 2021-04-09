class student:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def marks(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    class info:
        def __init__(self):
            self.school='montessori'
s1=student('satya',2)
s2=student('sai',3)
print('Name is ',s1.name,'roll no is ',s1.rno)
print('Name is ',s2.name,'roll no is ',s2.rno)
s1.marks(90,65,95)
s2.marks(55,66,33)
print('the average of ',s1.name,'is',s1.avg())
print('the average of ',s2.name,'is',s2.avg())
i=student.info()
print('The school is',i.school)
