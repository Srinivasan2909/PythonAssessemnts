##class product:
##    def __init__(self,pid,name,cost,brand,category,rating,discount):
##        self.pid=pid
##        self.name=name
##        self.cost=cost
##        self.brand=brand
##        self.category=category
##        self.rating=rating
##        self.discount=discount
##
##p1=product(1,"One plus8",20000,"one plus","mobile",2.9,21)
##p2=product(2,"bose1",10000,"bose","speaker",4.2,2)
##p3=product(3,"lg1",80000,"lg","washingmachine",2.2,29)
##p4=product(4,"timexxx",40000,"timex","watch",3.7,2)
##p5=product(5,"bose1",30000,"bose","speaker",2.0,31)
##p6=product(6,"samsung1",60000,"Sansung","mobile",4.9,25)
##p7=product(7,"zeb1",10000,"zebronic","speaker",1.3,27)
##p8=product(8,"ifb1",80000,"IFB","washingmachine",3.4,6)
##p9=product(9,"timeo",10000,"timex1","watch",3.1,21)
##p10=product(10,"bose1",40000,"bose","speaker",2.3,32)
##
##a=int(input("Enter your choice   "+"1-Sort by cost(Low to High)  2-Sort by cost(High to Low)  3-Sort by Rating   4-Sort by discounts(Low to High)  5-Sort by Dsicounts(High to low)"))
##sorttype=[["cost",False],["cost",True],["rating",False],["discount",False],["discount",True]]
##li=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
##li.sort(key=lambda el:el[sorttype[a-1][0]],reverse=sorttype[a-1][1])
##for i in li:
##    print(i["pid"]," ",i["name"],"  ",i["cost"],"    ",i["brand"],"  ",i["catogory"],"   ",i["rating"],"    ",i["discount"])

List=[]
class Product:
    def __init__(self,pid,name,cost,brand,category,rating,discount):
        self.pid=pid
        self.name=name
        self.cost=cost
        self.brand=brand
        self.category=category
        self.rating=rating
        self.discount=discount
        List.append(self)
    def choices(self,task):
        List2=[[self.cost,False],[self.cost,True],[self.rating,True],[self.discount,True],
               [self.discount,False]]
        return List2[task-1]
    def choicef(self,task):
        List2=[self.brand,self.category,self.name]
        return List2[task-1]
        
    def __str__(self):
        return "Name:"+str(self.name) +"    "+"Cost: Rs."+str(self.cost) +"    "+"Brand: "+self.brand +"    "+"Rating: "+str(self.rating)+"    "+"Discount: "+str(self.discount)+"%"
    
p1=Product(1,"Nokia 1100",1500,"Nokia","Electronics",5,50)
p2=Product(2,"Samsung A6",15000,"Samsung","Electronics",3,40)
p3=Product(3,"LG Washing Machine",12000,"LG","Home Appliance",4,70)
p4=Product(4,"T-shirt",800,"Puma","Fashion",2,80)
p5=Product(5,"Jeans",1200,"Nike","Fashion",2,20)
p6=Product(6,"Sofa",20000,"Oaktree","Furniture",3,40)

task=int(input("Enter 1 to sort price low to high\nEnter 2 to sort price high to low\nEnter 3 to sort rating high to low\nEnter 4 to sort discount low to high\nEnter 5 to sort price high to low\n"))
    
List3=[False,True,True,True,False]
List.sort(key=lambda el:el.choices(task)[0],reverse=List3[task-1])
print("The order of products based on your selection")
for i in List:
    print(i)








