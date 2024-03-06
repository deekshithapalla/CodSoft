import random
char="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#%$^&()_+}{:"
length=int(input("Enter the length of password:"))
x="".join(random.sample(char,length))
print(" Your password:",x)