students = [
    {
        "RollNo":1 , "Name":"Shivam", "M1":87 , "M2":45 ,"M3":65
    },
    {
        "RollNo":2 , "Name":"Shiv", "M1":23 , "M2":35 ,"M3":55
    },
    {
        "RollNo":3 , "Name":"Rohit", "M1":35 , "M2":25 ,"M3":66
    },
    {
        "RollNo":4 , "Name":"Shyam", "M1":90 , "M2":23 ,"M3":88
    },
    {
        "RollNo":5 , "Name":"Ramesh", "M1":34 , "M2":65 ,"M3":89
    }
]


# for i in students:
#     for key,values in i.items():
#         print(f"{key} : {values}")
#     print()




# user = int(input("Enter roll number :"))
# f = 0
# for i in students:
#     for key,values in i.items():
#         if values == user:
#             print(i)
#             f=1
# if f==0:
#     print("Roll Number not found")


user = int(input("Enter roll number :"))
sum = 0
for i in students:

    for key,values in i.items():
       if values == user:
            sum += i["M1"] + i["M2"] + i["M3"]
          
        
print(sum)




