# Concatenate Two Tuples

a = (101,102,103,104,105)
b = (105,107,108,109,110)
print("a :",a,"\n","b :",b)

con = a+b

print("The oncatenated tuple is",con)

print("---------------------------------------------")


# Find the Length of a Tuple

print("The length of a tuple is ",len(a))
print("The length of b tuple is ",len(b))
print("The length of concatenate is",len(con))




# Check if Two Tuples are Identical

print("----------------------------------------------")
print("Check if Two Tuples are Identical :")

c = (101,102,103)
d = (101,102,103)
print(c,d)

if c==d:
    print("The tuple c and d are identical")

else:
    print("The tuple is not identical")




