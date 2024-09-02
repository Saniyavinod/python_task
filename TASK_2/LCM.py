n1=int(input(" enter the number:"))
n2=int(input("enter the number"))

tn1=n1
tn2=n2
while n1%n2!=0:
    r=n1%n2
    n1=n2
    n2=r
gcd=n2
lcm=tn1*tn2/gcd
print(f"lcm of two numbers is {lcm}")    