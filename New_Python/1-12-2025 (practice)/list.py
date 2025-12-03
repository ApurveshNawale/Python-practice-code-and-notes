fruits = ["apple", "banana","mango","kiwi","orange" ]
print(fruits)

print("-------------------------------------------")


# replace fruit name with another name using index
print("replace fruit name with another name using index")
fruits [2] = "Cherry"
print(fruits)


# print length of fruits list
print(f"Length of Fruits :- {len(fruits)}")
print("-------------------------")

# Print all fruits using hango
print("using for loop in range")
for i in range(0,len(fruits)):
    print(fruits[i])

print("----------------------------------------")

print("using for each loop (for i in fruits)")
for i in fruits:
    print(i)


# print all fruits which fruit length

for i in fruits:
    if len(i) >= 5:
        print("the fruits length is greater than 5 is:", i)


# n = input("Enter the name of fruit : ")

# for i in range(0, len(fruits)):
#     if n[i] == fruits:
#         print(f"The fruit name is {fruits} ")



user_input = input("Enter any fruit name: ").lower()

if user_input in fruits:
    position = fruits.index(user_input) + 1
    print(f"{user_input} is present at {position} location")
else:
    print(f"{user_input} is not present")



