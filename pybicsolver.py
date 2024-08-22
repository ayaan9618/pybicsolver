# Simple calculator pybicsolver made by ayaan

print("Welcome to simple calculator pybicsolver")
print("This is basic calculator")
 
#asking values 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
#asking operation
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")



if choice == '1':
    print(num1, "+", num2, "=", num1 + num2)
elif choice == '2':
    print(num1, "-", num2, "=", num1 - num2)
elif choice == '3':
    print(num1, "*", num2, "=", num1 * num2)
elif choice == '4':
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Invalid input")
print("thanks for using pybicsolver calculator .To use again, Run again")