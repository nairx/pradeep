from calc_module import *

print("Math Calculator")
while True:
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    print("1.Add")
    print("2.Multiply")
    print("3.Subtract")
    print("4.Divide")
    print("5.Exit")
    choice = input("Enter your choice: ")
    if choice == "1" :
        result = add(x,y)
        print(f"Result is {result}")
    elif choice == "2":
        result = multiply(x,y)
        print(f"Result is {result}")
    elif choice == "3":
        result = subtract(x,y)
        print(f"Result is {result}")
    elif choice == "4":
        result = divide(x,y)
        print(f"Result is {result}")
    elif choice == "5":
        break
    else:
        print("Invalid Choice")