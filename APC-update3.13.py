# Thanks for all of the support on GitHub!
print("User 2264 Proudly Presents...")
print("Advanced Python Calcuator 3.13!")
print("Type any Character to start APC.")
startup = input()
import math
import cmath

# Function to perform basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Scientific functions
def square_root(x):
    if x < 0:
        return "Error! Cannot calculate the square root of a negative number."
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x, base=10):
    if x <= 0:
        return "Error! Logarithm of non-positive number is undefined."
    return math.log(x, base)

# Function for complex numbers
def complex_operations():
    real = float(input("Enter the real part: "))
    imag = float(input("Enter the imaginary part: "))
    cnum = complex(real, imag)
    return cnum

def complex_add(c1, c2):
    return c1 + c2

def complex_subtract(c1, c2):
    return c1 - c2

def complex_multiply(c1, c2):
    return c1 * c2

def complex_divide(c1, c2):
    if c2 == 0:
        return "Error! Cannot divide by zero."
    return c1 / c2

# Main calculator function
def advanced_calculator():
    print("Advanced Python Calculator")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Logarithm")
    print("11. Complex Number Operations")
    
    choice = input("Enter choice (1-11): ")

    if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        num1 = float(input("Enter first number: "))
        
        if choice in ['1', '2', '3', '4', '6']:
            num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"√{num1} = {square_root(num1)}")
        elif choice == '6':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        elif choice == '7':
            print(f"sin({num1}) = {sin(num1)}")
        elif choice == '8':
            print(f"cos({num1}) = {cos(num1)}")
        elif choice == '9':
            print(f"tan({num1}) = {tan(num1)}")
        elif choice == '10':
            base = float(input("Enter the base for the logarithm (default is 10): ") or 10)
            print(f"log({num1}) with base {base} = {log(num1, base)}")
    elif choice == '11':
        print("Complex number operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        sub_choice = input("Enter choice (1-4): ")

        cnum1 = complex_operations()
        cnum2 = complex_operations()
        
        if sub_choice == '1':
            print(f"({cnum1}) + ({cnum2}) = {complex_add(cnum1, cnum2)}")
        elif sub_choice == '2':
            print(f"({cnum1}) - ({cnum2}) = {complex_subtract(cnum1, cnum2)}")
        elif sub_choice == '3':
            print(f"({cnum1}) * ({cnum2}) = {complex_multiply(cnum1, cnum2)}")
        elif sub_choice == '4':
            print(f"({cnum1}) / ({cnum2}) = {complex_divide(cnum1, cnum2)}")
    else:
        print("Invalid input!")

# Running the calculator
if __name__ == "__main__":
    advanced_calculator()
print("Thanks for using APC!")
