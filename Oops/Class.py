class information:
    def __init__(self, id, Name, Salary):
        self.id = id
        self.Name = Name
        self.Salary = Salary

    # def BasicInfo(self):
    #     self.id = int(input("Enter your Id: "))
    #     self.Name = input("Enter your Name: ")
    #     self.Salary = float(input("Enter your Salary amount: "))
        # return self.id,self.Name,self.Salary
    
    def DisplayInfo(self):
        print("The Id is: ",self.id)
        print("The Name is: ",self.Name)
        print("The Salary is: ",self.Salary)

# Obj = information()
# MethodCall = Obj.BasicInfo()
# print("The Id is: ",Obj.id)
# print("The Name is: ",MethodCall[1]) 
# print("The Salary is: ",Obj.Salary)

obj2 = information(id=1, Name = "o", Salary=455)
# obj2.BasicInfo()
obj2.DisplayInfo()
# obj2.BasicInfo()
# print("The Id is: ",obj2.id)
# print("The Name is: ",obj2.Name)
# print("The Salary is: ",obj2.Salary)
# obj2.DisplayInfo()

