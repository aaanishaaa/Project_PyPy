def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2

def mod(n1, n2):
    return n1 % n2

def calculation(operation, number_1, number_2):
    if operation == '+':
        return add(number_1, number_2)
    elif operation == '-':
        return sub(number_1, number_2)
    elif operation == '*':
        return mul(number_1, number_2)
    elif operation == '/':
        return div(number_1, number_2)
    elif operation == '%':
        return mod(number_1, number_2)
    else:
        return "Invalid Operation"

number_1 = float(input("Enter your First Number: "))
number_2 = float(input("Enter your Second Number: "))
operation = input("Choose the operation (+, -, *, /, %): ")
ans = calculation(operation, number_1, number_2)
print(f"Result: {ans}")

while True:  #very important
    choice = input(f"Enter 'y' to continue operating on {ans}, or any other key to stop: ").lower()
    if choice == 'y':
        number_1 = ans 
        number_2 = float(input("Enter your Second Number: "))
        operation = input("Choose the operation (+, -, *, /, %): ")
        ans = calculation(operation, number_1, number_2)
        print(f"Result: {ans}")
    else:
        break
