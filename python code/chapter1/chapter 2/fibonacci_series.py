# n = 10
# num1 = 0
# num2 = 1
# next_number = num2
# count = 1 
# while count <= n:
#     print(next_number , end = " ")
#     count += 1
#     num1 , num2 = num2 , next_number
#     next_number = num1 + num2
# print()

a = 0
b = 1
n = 10
print("" , a , " " , end=" ")
for i in range(n):
    c = a+b;
    a=b;
    b=c;
    print(" ",c,end= "")
    