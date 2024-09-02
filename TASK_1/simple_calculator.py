# Get numbers from the user
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

# Display the menu of operations
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get the operation choice from the user
choice = input("Enter choice (1/2/3/4): ")

# Perform the selected operation and display the result
if choice == '1':
    result = n1 + n2
    print(f"{n1} + {n2} = {result}")
elif choice == '2':
    result = n1 - n2
    print(f"{n1} - {n2} = {result}")
elif choice == '3':
    result = n1 * n2
    print(f"{n1} * {n2} = {result}")
elif choice == '4':
    if n2 != 0:
        result = n1 / n2
        print(f"{n1} / {n2} = {result}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice. Please enter a number between 1 and 4.")
