class employee:
    def employee(self):
        eno=int(input('Enter the empno'))
        bsal=int(input('Enter the basic salary'))
        hra=bsal*12/100
        ta=bsal*15/100
        pf=bsal*20/100
        gsal=bsal+hra+ta
        nsal=gsal-pf
        print('rollno:',eno)
        print('basic salary:',bsal)
        print('hra:',hra)
        print('ta:',ta)
        print('pf:',pf)
        print('gsal:',gsal)
        print('nsal:',nsal)

e=employee()
e.employee()

