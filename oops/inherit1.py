class a:
    def run(self):
        for i in range(5):
            print('i=',i)
class b(a):
    def run1(self):
        for j in range(5):
            print('j=',j)

b1=b()
b1.run()
b1.run1()