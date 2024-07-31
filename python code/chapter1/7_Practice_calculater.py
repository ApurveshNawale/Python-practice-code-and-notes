first_number = int(input("Enter your first number : "))
operator = input("Enter operater(+,-,/,*,%) : ")
second_number = int(input("Enter your second number : "))

if operator == '+':
    print(first_number + second_number)

elif operator == '-':
    print(first_number - second_number)

elif operator == '*':
    print(first_number * second_number)

elif operator == '/':
    print(first_number / second_number)

elif operator == '%':
    print(first_number % second_number)

else:
    print("This ia invalid number")