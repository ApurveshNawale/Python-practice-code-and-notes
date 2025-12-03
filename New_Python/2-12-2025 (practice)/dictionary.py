fruits = {
"apple" : 200,
"mango" : 500,
"cherry" : 340,
"orange" : 100,
"banana" : 60
}


#iterate Dictionary
for key,value in fruits.items():
    print(f"{key} price is {value}")


#addition prices
sum=0
for i in fruits.values():
    sum+=i
print(f"sum of all prices is: {sum}")


# #Ask the user to enter key and print corrosponding value of the key
# k = input("Enter any fruit name : ")

# for key,value in fruits.items():
#     if k == key:
#         print(f"the fruit {key} is present and the price is {value}")
#         break
# else:
#     print("fruit is not found")

print("--------------------------")


# print highest price fruit name
max = 0
for key,value in fruits.items():
    if value > max:
        max = value
        k = key
print(f"the high price is {max} and the fruit is {k}")