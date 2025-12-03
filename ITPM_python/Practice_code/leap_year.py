# Check if a Year is a Leap Year

a = int(input("Enter Year : "))

if  a % 400 == 0:
    print(a,"This Year is Leap Year")


elif  a %4==0 and a%100 != 0:
    print(a,"This Year is Leap Year")

else:
    print("This is Not Leap Year")

