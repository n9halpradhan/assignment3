n=int(input("Enter a number: "))
temp=n
s=0
for i in range(1,n+1):
    if n==0:
        print(0)
    elif n<0:
        print("Error 404!")
    else:
        s+=n
        n-=1
print("The sum of first",temp,"number is:",s)