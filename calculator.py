#calculator

a=int(input("enter a number a"))
b=int(input("enter a number b"))

op=input("enter an operator(+ or - or / or *)")

if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="/":
    print(a/b)
elif op=="*":
    print(a*b)
else:
    print("please enter an operator!")
