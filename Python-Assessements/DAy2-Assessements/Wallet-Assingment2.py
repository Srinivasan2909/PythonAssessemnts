def createwallet(balance,username,pin):
    
    def deposit(amount):
        nonlocal balance
        balance=balance+amount
        print("Hello",username,",",amount,"is deposited successfully")

    def withdraw(amount):
        nonlocal balance
        balance=balance-amount
        print("Hello",username,",",amount,"is withdrawn successfully")
    
    def checkbal():
        nonlocal balance
        print("Hello",username,",","your balance is",balance)
    

    def transfer(username,amount):
        nonlocal balance
        balance=balance-amount
        print("Hello!","Transfer to",username,"of Rs.",amount,"is done successfully")
        username[0](amount)
        
        
                 
    return [deposit,withdraw,checkbal,transfer]


        
w1=createwallet(10000,"Srini",1234)
w2=createwallet(5000,"varun",5678)
w3=createwallet(2000,"harsha",987)
##pin=int(input("Enter the pin"))
##if(pin==1234):
##        
##    a=int(input("Hello Srini:   What do you want to do?1-Deposit   2-Withdraw 3-Check balance 4-transfer funds"))
##    if a==1:
##        amt=int(input("Enter the amount to deposit"))
##        w1[0](amt)
##        
##    elif a==2:
##        amt=int(input("Enter the ampunt to withdraw"))
##        w1[1](amt)
##    elif a==3:
##        w1[2]()
##    elif a==4:
##        usr=input("Enter the user you want to transfer")
##        amt=int(input("enter the amount you want to transfer"))
##        if(usr=="varun"):
##            w1[3](w2,amt)
##        elif(usr=="harsha"):
##            w1[3](w3,amt)

###pin=int(input("Enter the pin"))
###if(pin==1234):
w1[0](500)
w1[1](300)
w1[2]()
w1[3](w2,800)
w1[2]()
##
##
###else:
###print("Wrong pin")
##    
##
##
####pin=int(input("Enter the pin"))
####if(pin==5678):
w2[2]()
w2[2]()
w2[3](w1,100)
w2[2]()
w1[2]()    

    
    


