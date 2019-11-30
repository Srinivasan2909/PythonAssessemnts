days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
entereddate=int(input("Enter the date"))
if(entereddate >0 & entereddate<31):
    print(days[(entereddate+3)%7])
else:
    print("Invalid date")
