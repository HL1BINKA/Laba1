a=int(input("Enter a: "))
b=int(input("Enter b: "))
if a<0 or b<0:
    print("Error!")
else:
    if a>b:
        X=a*b/21;
        print(X," = ",a," * ",b," / 21")
    elif a == b :
        X=-5;
        print(X)
    else:
        X=3*a/b+1;
        print(X," =  3 * ",a," / ",b," + 1")

        