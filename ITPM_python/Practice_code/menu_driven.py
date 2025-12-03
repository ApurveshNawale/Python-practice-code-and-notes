while True:
    print("--------------------------------------------------")
    print("------Menu-----")
    print("1.Prime Number")
    print("2.Amstrong Number")
    print("3.Palendrome")
    print("4.reverse the number")
    print("Exit")
    print("-----------------------------------------------------")

    choice = int(input("Enter your choice : "))

    print("-------------------------------------------------")

    if (choice == 1):
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
        
    elif(choice == 2):

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

    elif (choice == 3):
        num = input("Enter a number: ")
        if num == num[::-1]:
            print(num, "is a Palindrome.")
        else:
            print(num, "is not a Palindrome.")

    elif (choice == 4):
        num = input("Enter a number: ")
        print("Reversed number is:", num[::-1])

    elif (choice == 5):
        exit()

    else:
        print("Invalid Choice")