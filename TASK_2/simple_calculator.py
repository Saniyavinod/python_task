
num1=int(input("enter the number :"))

num2=int(input("enter the number :"))

print("1.add")
print("2.sub")
print("3.mul")
print("4.division")

choice=int(input("choice: 1/2/3/4"))

if choice==1:
    result=num1+num2
    print(result)
elif choice==2:
    result=num1-num2
    print(result)
elif choice==3:
    result=num1*num2
    print(result)
elif choice==4:
    result=num1//num2
    print(result)    

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice. Please enter a number between 1 and 4.")

