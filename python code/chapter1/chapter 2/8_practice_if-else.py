## nesting

n = int(input("Enter Your no : "))
if n <= -1 :
    print("Negative")

elif n >= 1:
    print("positive")

    if n >= 50 :
        print("Number is grater than 50")
    else :
        print("Number is less than 50")
else : 
    print("0")