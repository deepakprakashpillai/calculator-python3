def add(x, y):
    return x + y


print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
    else:
        print("Invalid input")

    another_calculation = input(
        "Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break
