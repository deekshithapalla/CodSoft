def add(a,b):
    z=a+b
    return z
def sub(a,b):
    y=a-b
    return y
def mul(a,b):
    x=a*b
    return x
def div(a,b):
    p=a/b
    return p
def mod(a,b):
    q=a%b
    return q
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print("1.ADD","2.SUBTRACT","3.MULTIPLICATION","4.DIVISON","5.MODULUS")
choice=int(input("Enter your choice:"))
if choice==1:
    print(add(a,b))
elif choice==2:
    print(sub(a,b))
elif choice==3:
    print(mul(a,b))
elif choice==4:
    print(div(a,b))
elif choice==5:
    print(mod(a,b))
else:
    print("Enter correct choice!!")