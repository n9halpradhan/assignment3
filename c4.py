f=1
n=int(input("Enter the number: "))
if n<0:
   print("Factorial is defined only for non negative number")
elif n==0:
   print("Factorial for 0 is 1")
else:
   for i in range(1,n+1):
        f*=i
   print("Factorial: ",f)