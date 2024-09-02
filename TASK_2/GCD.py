n1=int(input(" enter the number:"))
n2=int(input("enter the number"))
while n1%n2!=0:
    r=n1%n2
    n1=n2
    n2=r
gcd=n2    
print(f"gcd of twoo number is : {gcd}")    

