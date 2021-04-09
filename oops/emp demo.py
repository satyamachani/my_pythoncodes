class employee:
    def employee(self,rno,bsal):
        self.rno=rno
        self.bsal=bsal
        
    def printf(self):
        hra=self.bsal*12/100
        ta=self.bsal*15/100
        pf=self.bsal*20/100
        gsal=self.bsal+hra+ta
        nsal=gsal-pf 
        print('rollno:',self.rno)
        print('basic salary:',self.bsal)
        print('hra:',hra)
        print('ta:',ta)
        print('pf:',pf)
        print('gsal:',gsal)
        print('nsal:',nsal)

e=employee()
e.employee(101,25000)
e.printf()
