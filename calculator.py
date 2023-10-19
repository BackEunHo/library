# 코드 교체 부분
def add(x, y):
    """This function adds two numbers"""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y

def divide(x, y):
    """This function divides two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation -\n"
        "1. Add\n"
        "2. Subtract\n"
        "3. Multiply\n"
        "4. Divide\n")

choice = input("Enter choice (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        try:
            print(num1, "/", num2, "=", divide(num1, num2))
        except ValueError as e:
            print(e)
else:
    print("Invalid Input")
