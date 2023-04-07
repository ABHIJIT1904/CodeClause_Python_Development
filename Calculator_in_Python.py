print("CALCULATOR IN PYTHON")

no1=int(input("Enter First No :"))
no2=int(input("Enter Second No :"))
a=int(input("Press 1:Addition\nPress 2:Substraction\nPress 3:Multiplication\nPress 4:Division\nPress 0:Exit \n"))
while a>=5 or a<0:
    print("Invalid Input")
    print("Please Choose From Below Option")
    a=int(input("Press 1:Addition\nPress 2:Substraction\nPress 3:Multiplication\nPress 4:Division\nPress 0:Exit \n"))

if a==1:
    print("Ans :",no1+no2)
elif a==2:
    print("Ans :",no1-no2)
elif a==3:
    print("Ans :",no1*no2)
elif a==4:
    print("Float Division Ans :",no1/no2)
    print("Integer Division Ans :",no1//no2)
elif a==0:
    exit()
