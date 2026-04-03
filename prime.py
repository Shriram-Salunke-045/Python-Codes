num = int(input("Enter the number: "))

if(num<2):
   print("not prime")
else:
   for i in range(2,int(num**0.5)+1):
      if(num % i==0):
         print("Not Prime")
         break
   else:
      print("prime")