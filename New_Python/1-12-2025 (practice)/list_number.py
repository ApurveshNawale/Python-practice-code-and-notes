number = [22,33,11,44,55,66,66,67]


# print only even numbers frcyn numbers list
for i in number:
    if i%2==0:
        print(i)


# get even numbers and add into even _ list and vice versa
even_list = []
odd_list =[]

for i in number:
    if i%2==0:
        even_list.append(i)

    else:
        odd_list.append(i)

print(f"the even list is {even_list}")
print(f"The odd list is {odd_list}")


#print max number in list
max = number[0]

for i in number:
    if i > max:
        max=i
print(f"the max number is {max}")