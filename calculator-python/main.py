print("=======================")
print("Welcome To calculator!")
print("=======================")

def main():
    # Read a numeric value from user and store in variable A
    a = float(input("Enter value A: "))
 
    # Read a numeric value from user and store in variable B
    b = float(input("Enter value B: "))
 
    # Select a mathematical operator
    operator = input("Select operation (+, -, *, /): ").strip()
 
    # If Operator is '+' ?
    if operator == "+":
        # Add A and B, store result in C
        c = a + b
        print("Result =", c)
 
    # If Operator is '-' ?
    elif operator == "-":
        # Subtract B from A, store result in C
        c = a - b
        print("Result =", c)
 
    # If Operator is '*' ?
    elif operator == "*":
        # Multiply A and B, store result in C
        c = a * b
        print("Result =", c)
 
    # If Operator is '/' ?
    elif operator == "/":
        # Is B == 0 ?
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            # Divide A by B, store result in C
            c = a / b
            print("Result =", c)
 
    # Invalid operator
    else:
        print("Error: Invalid operator. Please enter +, -, *, or /.")
 
if __name__ == "__main__":
    main()