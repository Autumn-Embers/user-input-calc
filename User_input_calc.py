# Function that calculates addition with two numbers
def add(x, y):
    return x + y

# Function that calculates subtraction with two numbers
def subtract(x, y):
    return x - y

# Function that calculates multiplication with two numbers
def multiply(x, y):
    return x * y

# Function that calculates division with two numbers
def divide(x, y):
    return x // y

# Function that calculates the remainder of division with two numbers
def remainder(x, y):
    return x % y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide and Remainder")
print("5.Cancel")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    if choice > '5':
        print("error please select a valid option.")

    if choice < '1':
        print("error please select a valid option.")    

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4',):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("invalid input please enter a number instead.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print("Division", num1, "//", num2, "=", divide(num1, num2))
            print("Remainder", num1, "%", num2, "=", remainder(num1, num2))
    
            
    if choice in('5'):
        print("Calculator Closed")
        break