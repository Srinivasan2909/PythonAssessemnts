d={"Srini":"qwerty123","Rakesh":"rakesh"}
username=input("Enter username")
password=input("Enter passowrd")
try:
    if username not in d or password not in d[username]:
        raise Exception("Invalid Cridentials")
    else:
        print("Hello"+username)
except Exception as e:
    print("Generic Exception:",e)

