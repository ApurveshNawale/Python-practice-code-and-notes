while True:
    print("\n------ Menu ------")
    print("1. Prime Number")
    print("2. Armstrong Number")
    print("3. Palindrome")
    print("4. Reverse the Number")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Prime Number
    if choice == '1':
        num = int(input("Enter a number: "))
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    print(num, "is not a prime number.")
                    break
            else:
                print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")

    # Armstrong Number
    elif choice == '2':
        num = int(input("Enter a number: "))
        temp = num
        sum = 0
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10
        if sum == num:
            print(num, "is an Armstrong number.")
        else:
            print(num, "is not an Armstrong number.")

    # Palindrome
    elif choice == '3':
        num = input("Enter a number: ")
        if num == num[::-1]:
            print(num, "is a Palindrome.")
        else:
            print(num, "is not a Palindrome.")

    # Reverse Number
    elif choice == '4':
        num = input("Enter a number: ")
        print("Reversed number is:", num[::-1])

    # Exit
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
