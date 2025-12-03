# 1. Age Validation

# Write a Python program that asks the user to enter their age.
# If the entered age is less than 18, raise a custom exception named UnderAgeError.
# Your program should display a meaningful message explaining why the user is not eligible.
# If the age is 18 or above, print a success message.

class UnderAgeExeption(Exception):
    pass

try:
    age = int (input("Enter you Age = "))

    if age >= 18 :
        print (" Your Eligible for vote ....")

    else:
        raise UnderAgeExeption

except UnderAgeExeption :
    print ("Your note eligible for vote....")

finally:
    print (" Becouse your age is",age)