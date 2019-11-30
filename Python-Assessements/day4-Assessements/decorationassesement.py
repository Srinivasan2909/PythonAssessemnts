def outer(a):
    def inner(*args, **kwargs):
          for arg in args:
            if not isinstance(arg, str):
                print("Not all arguments are string")
                return

          for kwarg in kwargs.values():
            if not isinstance(kwarg, str):
                print("Not all arguments are string")
                return

          else:
            a(*args, **kwargs)
    return inner


@outer
def function1(str1, str2, str3):
    print(str1, str2, str3)

@outer
def function2(a, b, c):
    print(a, b, c)

@outer
def function3(name1, name2):
    print(name1, name2)


function1(str1 = "Srini", str2 = "Vasan", str3 = "Srini")
function2(1, "Hello", "harry")
function3("ben", name2 = "cat")
