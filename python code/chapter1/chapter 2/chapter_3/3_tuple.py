#### tuple

# A tuple is a built-in data structure in Python that is used to store a collection of items. 
# It is similar to a list, but unlike lists, tuples are immutable, meaning that once a tuple is created, its elements cannot be changed.

marks = (95 , 96, 96 , 96, 45)  #Tuples are defined by enclosing the elements in parentheses ().
print(type(marks))

print(marks.count(96))
print(marks.index(96))

print("------------------------------------------------------------------")

#### set

marks = {95 , 96, 96 , 96, 45}   ## it do not allow duplicate elements. 
print(marks)                     ## set are defined by enclosing the elements in  {}

print("------------------------------------------------------------------")


#### Dictionary

marks = {"physics" : 98 , "chemistry" : 89 }
print(marks["chemistry"])

marks["english"] = 98 ;
print(marks)

marks["english"] = 56
print(marks)