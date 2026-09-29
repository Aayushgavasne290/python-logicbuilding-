choice=0
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
while choice != 4:
    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. division")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Addition:", a+b)
    elif choice==2:
        print("Subtraction:", a-b)
    elif choice==3:
        print("Multiplication:", a*b)
    elif choice==4:
        print("divsionl:",a/b)
    else:
        print("Invalid choice. Please try again.")