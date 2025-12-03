'''
mode
file must exist.
"r" = Read =
"w" = Write
= Creates new file or overwrites the existing.
= Append = Adds data at the end
"x" = create
= creates file, error if file exists.
"b" - binary
=for images, videos
"t" = Text [default]
= read+write = file must exist
"w+" =write+read =
overwrites
hppend + Read

'''

# Read file


# file = open("demo.txt","r")
# print(file.read())
# file.close()

# file = open("demo.txt","r")
# print(file.read(10))
# file.close()

# file = open("demo.text","r")
# print(file.read(10)) #o/p = This is Fi
# file.close()

# file = open("demo.text","r")
# print(file.readline()) #o/p = This is File Handling and its a 1st Line.
# file.close()

file = open("demo.txt","r")
print(file.readlines()) #o/p = ['This is File Handling and its a 1st Line.\n', 'This is 2nd Line. \n', 'This is 3rd Line']
file.close()

# file = open("demo.txt", "r")
# print(file.readline())


