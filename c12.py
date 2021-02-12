l=int(input("How many terms? "))
x=0
y=1
count=0
if l==1:
   print("Fibonacci series upto",l,":")
   print(x)
else:
   print("Fibonacci series: ")
   while count<l:
       print(x,end=" ")
       z=x+y
       x=y
       y=z
       count+=1
