count=0
def sayhi():
    global count
    count=count+1
sayhi()
sayhi()
sayhi()
print("Count:",count)

#using non local
def outer():
    count=0
    def inner():
        nonlocal count
        count+=1
       
    return inner
hello=outer()
hello()
hello()
hello()
outer()
hello()
hello()
print(count)


