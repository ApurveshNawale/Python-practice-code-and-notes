list = [2 , 1 , 3]

list.append(4)  #adds one element at the end [2 , 1 , 3 , ,4]
print(list)

list.sort()   #sorts in ascending order [1 , 2 , 3 , 4]
print(list)

list.sort(reverse=True)   #sorts in descending order [4 , 3 , 2 , 1]
print(list)

list.insert(0,5)   #insert element at index [5 , 4 , 3 , 2 , 1]
print(list)

list.reverse()  #reverses list[1 , 2 , 3 , 4 , 5]
print(list)

list.remove(5)   #removes first occurrence of element [1 , 2 , 3 , 4]
print(list)

list.pop(3)     #removes element at idx [1 , 2 , 3]
print(list)