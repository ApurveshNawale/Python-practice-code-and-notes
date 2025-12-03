# Find the Index of an Element in a Tuple

n = (101,102,103,104,105,106,108,1012,1232,1245,5656,64576,2342,35435,654645)
print(n)

num = int(input("Enter Number to find its index : "))

if num in n:
    print(num,"is in index number",n.index(num))

else:
    print(num,"is not in tuple")

