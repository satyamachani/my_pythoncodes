class JaganCons1:
    
    def JaganCons12(self,x,y,z):
        self.x=x;
        self.y=y;
        self.z=z;
    def JaganCons1(self):
        self.x=-1
        self.y=-1
        self.z=-1
    

c=JaganCons1()
c.JaganCons12(10,10,15)
print("x :",c.x,", y:",c.y)
print("x :",c.x,", y:",c.z)
c.JaganCons1()
print("x :",c.x,", y:",c.x)
