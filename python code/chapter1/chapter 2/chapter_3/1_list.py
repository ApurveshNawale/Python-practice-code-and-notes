#### list

marks = [95 , 96 , 54 , 56 , 33]  #list are defined by enclosing the elements in  [].

print(type(marks))

marks.insert(0,1)
marks.append(69)

print( marks)  
print(len(marks))


print()

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


print()

