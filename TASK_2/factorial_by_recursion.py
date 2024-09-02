def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
    
n=int(input("enter the number:"))

if n<=0:
    print("doesn't exist")
else:
    print(f"factoral of {n} is {fact(n)}")    
    