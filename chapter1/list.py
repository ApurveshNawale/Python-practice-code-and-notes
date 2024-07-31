#### list

marks = [95 , 96 , 54 , 56 , 33]  #list are defined by enclosing the elements in  [].

marks.insert(0,1)
marks.append(69)

print( marks) 
print(len(marks))


print("------------------------------------------------------------------")

#### Break and continue

students = ["raj" , "shyam", "jiten" , "apurvesh"]   ## The break statement is used to exit the loop completely, 
for student in students :                            ## regardless of the loop's condition
    if student == "jiten":
       break ; 
    print(student)

print()

students = ["raj" , "shyam", "jiten" , "apurvesh"]    ## The continue statement is used to skip the rest of the code 
for student in students :                             ## inside the loop for the current iteration and move on to the next iteration.
    if student == "shyam":
       continue ; 
    print(student)


print("------------------------------------------------------------------")

#### tuple

# A tuple is a built-in data structure in Python that is used to store a collection of items. 
# It is similar to a list, but unlike lists, tuples are immutable, meaning that once a tuple is created, its elements cannot be changed.

marks = (95 , 96, 96 , 96, 45)  #Tuples are defined by enclosing the elements in parentheses ().
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