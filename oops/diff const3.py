class Jaganover:
   
    def Jaganover(self,prodname,prodqty,prodprice,nbill):
        self.pname=prodname;
        self.qty=prodqty;
        self.price=prodprice;
        self.bill=nbill;
	
    def Jaganover1(self,p,p1name,b):
        self.pname=p1name;
        self.price=p;
        self.qty=b/p;
        self.bill=b;
	
    def Jaganover2(self,ppname,pprice,b1):
        self.pname=ppname;
        self.price=(int)(pprice-(0.1));
        self.bill=b1;
	
    def print(self):
        print("Product name:" ,self.pname)
        print("Quantity:",self.qty)
        print("Price:",self.price)
        print("Bill:",self.bill)
prods = Jaganover()
prods.Jaganover('apples',5,20,20*5)
prods.print()
prods.Jaganover1(10,"Oranges",10*5)
prods.print()
prods.Jaganover2("Grapes",25,20*10)
prods.print()
