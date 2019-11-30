li=[{"pid":1,"name":"timex1","cost":800,"brand":"timex","catogory":"watches","rating":4,"discount":20},
      {"pid":2,"name":"casio400","cost":1200,"brand":"casio","catogory":"watches","rating":4.5,"discount":25},
      {"pid":3,"name":"bosch6","cost":24000,"brand":"bosch","catogory":"washing machine","rating":3.8,"discount":15},
      {"pid":4,"name":"whirlpool9","cost":27000,"brand":"whirlpool","catogory":"washing machine","rating":4,"discount":20},
      {"pid":5,"name":"motog2","cost":8000,"brand":"motorola","catogory":"mobiles","rating":3.5,"discount":10},
      {"pid":6,"name":"iphone11","cost":65000,"brand":"apple","catogory":"mobiles","rating":4.5,"discount":17},
      {"pid":7,"name":"mi7","cost":400,"brand":"mi","catogory":"earphones","rating":4.4,"discount":9},
      {"pid":8,"name":"zebronics3","cost":700,"brand":"zebronics","catogory":"earphones","rating":4,"discount":25}]

a=int(input("Enter your choice   "+"1-Sort by cost(Low to High)  2-Sort by cost(High to Low)  3-Sort by Rating   4-Sort by discounts(Low to High)  5-Sort by Dsicounts(High to low)"))
sorttype=[["cost",False],["cost",True],["rating",False],["discount",False],["discount",True]]
li.sort(key=lambda el:el[sorttype[a-1][0]],reverse=sorttype[a-1][1])
for i in li:
    print(i["name"],"  ",i["cost"],"    ",i["brand"],"  ",i["catogory"],"   ",i["rating"],"    ",i["discount"])
    
print("0.brand,1.catogory,2.name")
number2=int(input("enter the number from 0 to 2"))


string1=input("enter something for filtering")
List3=["brand","catogory","name"]
l=List3[number2]
newobj=filter(lambda el:el[l]==string1,li)
for i in newobj:
    print('{name} {cost} {brand} {catogory} {rating} {discount}'.format(**i))           
##if(a==1):
##      li.sort(key=lambda el:el["cost"])
##      print(li)
##          
##elif(a==2):
##    li.sort(key=lambda el:el["cost"],reverse=True)
##    print(li)
##    
##elif(a==3):
##    li.sort(key=lambda el:el["rating"])
##    print(li)
##    
##elif(a==4):
##    li.sort(key=lambda q:q["discount"])
##    print(li)
##    
##elif(a==5):
##    li.sort(key=lambda el:el["discount"],reverse=True)
##    print(li)
##    
##else:
##    print("Wrong choice")
##    
##b=int(input("Enter your choice for filtering:"+"1-Filter by category"+"2-Filter by brand"+"Filter by name"))
##if(a==1):
##    newli=filter(lambda el:el["category"]=="mobiles",li)
##    for i in newli:
##        print('{name} {cost}'.format(**i))


