# Check if a Number is Divisible by Both 3 and 5.

a = int(input("Enter Number :"))

if a%3 == 0 and a%5 == 0:
    print(a,"is Divisible by Both 3 and 5")

elif a%3 ==0:
    print(a,"is Divisible By 3")

else:
    print(a,"is Divisibale by 5")
