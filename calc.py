op=input("Enter the operation to be done")
a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
num =int(input("Enter the number of times to be calculated:"))
i=1
while(i<=num):
    if(op=="Add"):
        print("Sum=",a+b)
    elif(op=="-"):
        print("Difference=",a-b)
    elif(op=="*"):
        print("Product=",a*b)
    elif(op=="/"):
        print("Quotient=",a/b)
    elif(op=="%"):
        print("Remainder=",a%b)
    else:
        print("invalid operation")
