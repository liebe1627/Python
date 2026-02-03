class Arithmatic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first number: "))
        self.Value2 = int(input("Enter second number: "))
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2
    
Obj1 = Arithmatic()
Obj1.Accept()
print("Addition is: ",Obj1.Addition())
print("Subtraction is: ",Obj1.Subtraction())
print("Multiplication is: ",Obj1.Multiplication())
print("Division is: ",Obj1.Division())



