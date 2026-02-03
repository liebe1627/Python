class Demo:
    
    Value = 0

    def __init__(self,No1,No2):
        self.No1 = No1
        self.No2 = No2

    def fun(self):
        print("First value: ",self.No1)
        print("Second value: ",self.No2)
    
    def gun(self):
        print("First value: ",self.No1)
        print("Second value: ",self.No2)

Obj1 = Demo(11,10)
Obj2 = Demo(51,101)

Obj1.fun()
Obj1.gun()
Obj2.fun()
Obj2.gun()
