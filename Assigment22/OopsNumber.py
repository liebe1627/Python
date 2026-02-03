class Numbers:

    def __init__(self,Value):
        self.Value = Value
       
    def chkprime(self):
        
        if self.Value<=1:
            print("Not prime")
            return False
        
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False
        return True
    
    def perfect(self):
        sumNo = 0
        for i in range(1,self.Value):
            if self.Value % i == 0:
                sumNo +=i
        if sumNo == self.Value:
            return True
        else:
            return False
    
    def factor(self):
        for i in range(1,self.Value+1):
            if self.Value % i == 0 :
                print("The factors are: ",i)
        
    def sumfactor(self):
        sumNo = 0
        for i in range(1,self.Value+1):
            if self.Value % i == 0 :
                sumNo += i
        print("Sum of factor is: ",sumNo)
                 
Value = int(input("Enter a number : "))
obj1 = Numbers(Value)

print("Prime: ",obj1.chkprime())
print("Perfect: ",obj1.perfect())
obj1.factor()
obj1.sumfactor()    