# Grade students based on marks
# marks >= 90, grade =“A”
# 90 > marks >= 80, grade =“B”
# 80 > marks >= 70, grade =“C”
# 70 > marks, grade = "D"

grade = int(input("Enter your marks : "))
if grade >= 90 :
    print("Your Grade is A "  )
elif grade < 90 and grade >= 80 :
    print("your Grade is B ")
elif grade < 80 and grade >= 70 :
    print("your Grade is C " )
else :
    print("Your Grade is D ")