#### String function


## str.endsWith("be") #returns true if string ends with substr
str = "I am studing a python from youtube"
print(str.endswith("ube"))             


## str.capitalize( ) #capitalizes 1st char
print(str.capitalize())  ## this change can only one time. it create new string and make changes
str = str.capitalize()   ##  this line modify oringinl string and return value
print(str )


##str.replace( old, new ) #replaces all occurrences of old with new
print(str.replace("python" , "java"))


##str.find( word ) #returns 1st index of 1st occurrence
print(str.find("m"))


##str.count(“am“) #counts the occurrence of substr in string
print(str.count("a"))
