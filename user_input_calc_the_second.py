# Function that calculates addition with two numbers
def sum(x, y):
    return x + y

# Function that calculates subtraction with two numbers
def difference(x, y):
    return x - y

# Function that calculates multiplication with two numbers
def product(x, y):
    return x * y

# Function that calculates division with two numbers
def quotient(x, y):
    return x // y

# Function that calculates the remainder of division with two numbers
def remainder(x, y):
    return x % y


print("Select operation.")
print("1.Input two numbers for calculations.")
print("2.Or cancel.")

while True:
    # take input from the user
    choice = input("Enter choice(1/2): ")
    if choice < '1':
        print("error please select a valid option.")
    if choice > '1':
        print("error please select a valid option.")
    # check if choice is one of the four options
    if choice in ('1'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print ("Results:")
            print ("Sum:", sum(num1, num2))
            print ("Difference:", difference(num1, num2))
            print ("Product:", product(num1, num2))
            print ("Quotient:", quotient(num1, num2))
            print ("Remainder:", remainder(num1, num2))

    if choice in('2'):
            print("Calculator Closed")
            break