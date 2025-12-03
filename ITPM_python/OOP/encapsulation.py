#1.Encapsulation:- # public , private() , protected(_)
class Encap:
    def __init(self,a,b):
        self.a = a
        self.b = b
        print("1.This is Encap Class Constructor..!")

    def showData(self):
        print(f"Value of a={self.a},value of b={self.b}")

e=Encap(10,20)
e.showData() #o/p = Value of a=10,value of b=20 as it is a Public parameters/variables
print("value of A=",e.a)

# #2.Private()
class Encap:
    def __init(self,a,b):
        self.a = a
        self.__b = b
        print("1.This is Encap Class Constructor..!")

    def showData(self):
        print(f"Value of a={self.__a},value of b={self.__b}")
e=Encap(20,30)
# print("value of A=",e.a) #we're accessing variable/param outside the class
e.showData()

#3.Protected(_)
class Encap:
    def __init(self,a,b,c):
        self.__a = a
        self.__b = b
        self._c=c
        print("1.This is Encap Class Constructor..!")

    def showData(self):
        print(f"Value of a={self.__a},value of b={self.__b},value of c={self._c}")
e=Encap(20,30,40)
# print("value of A=",e.a) #we're accessing variable/param outside the class
e.showData()
# print("value of C=", e.c)