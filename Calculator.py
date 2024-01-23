def add(x , y):
    return x + y
def subtract(x , y):
    return x - y
def multiply(x , y):
    return x * y
def divide(x , y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Error! Division by zero is not allowed.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
while True:
    choice = float(input("Enter your choice (1/2/3/4): "))
    if choice in (1, 2, 3, 4):
        try:
            num1 = eval(input('Enter first number :'))
            num2 = eval(input('Enter second number :'))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        if choice == 1:
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice ==2:
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice == 3:
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice == 4:
            try:
                print(num1,"/",num2,"=",divide(num1,num2))
            except ValueError as e:
                print(e)
                continue
        next_calculation = input("Want to do next calculation? (y/n): ")
        if next_calculation=='n':
            break
    else:
        print("Invalid Input! Please Enter the correct option (1/2/3/4).")
