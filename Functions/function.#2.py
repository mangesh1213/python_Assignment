def addbyten(x,y,z):
    x+=10
    y+=10
    z+=10
    return x,y,z

a=int(input("Enter value for x"))
b=int(input("Enter value for y "))
c=int(input("Enter value for z"))

p,q,r=addbyten(a,b,c)
print(p)
print(q)
print(r)
