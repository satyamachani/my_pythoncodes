class a:
    def a(self):
        print("super cnstr")
class b(a):
    def b(self):
        print("sub cnstr")
b1 = b();
b1.b()
b1.a()
