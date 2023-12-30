import math as m
n1=int(input("enter the num1:"))
n2=int(input("enter the num2:"))
operation=input("enter the operation you want:")
if operation=="+":
    print(n1+n2)
elif operation=="-":
    print(n1-n2)
elif operation=="*":
    print(n1*n2)
elif operation=="/":
    print(n1/n2)
elif operation=="//":
    print(n1//n2)
elif operation=="%":
    print(n1%n2)
elif operation=="^":
    print(m.pow(n1,n2))
else :
    print('invalid operation')