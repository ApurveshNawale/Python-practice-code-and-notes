class InvalidMarks(Exception):
    pass

try:
    marks = int (input("Enter you marks = "))

    if marks >= 0 and marks <= 100 :
        print (" Your pass ....")

    else:
        raise InvalidMarks

except InvalidMarks :
    print ("valid range is Between 0 and 100")

finally:
    if marks >= 0 and marks <= 100 :
     print (" your marks is",marks)

    else:
        print("becouse your marks is ", marks)