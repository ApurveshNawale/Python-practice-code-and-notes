class Father:
    def init(self):
        print("1.This is Father Class Constructor")

    def assets1(self):
        print( f"Father is having Flat.")
    

class Mother: 
    def init(self):
        print("2.This is Mother Class Constructor")

    def assets2(self):
        print(f"Mother is having Gold.")
    
class Child(Father,Mother):
    def init(self):
        Father.init(self) #we're executing constructor of both classes
        Mother.init(self)
        print("3.This is Child Class Constructor")
    
    def totalAsset(self):
        super().assets1()
        super().assets2()
        

newChild=Child()
newChild.totalAsset()
print(newChild.totalAsset())