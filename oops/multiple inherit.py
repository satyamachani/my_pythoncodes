# here a and b are separate classes and c inherits both and b
class a:
    def satya(self):
        print('this is satya')
class b:
    def sai(self):
        print('this is sai')
class c(a,b):
    def jagan(self):
        print('this is jagan')
s=c()
s.satya()
s.sai()
s.jagan()