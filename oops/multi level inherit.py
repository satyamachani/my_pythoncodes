# b inherits a and c inherits both a and b
class a:
    def satya(self):
        print('this is satya')
class b(a):
    def sai(self):
        print('this is sai')
class c(b):
    def jagan(self):
        print('this is jagan')
s=c()
s.satya()
s.sai()
s.jagan()
d=b()
d.satya()
d.sai()